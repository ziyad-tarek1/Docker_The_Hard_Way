package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/containerd/containerd"
	"github.com/containerd/containerd/cio"
	"github.com/containerd/containerd/namespaces"
	"github.com/containerd/containerd/oci"
)

func main() {
	if len(os.Args) < 3 {
		log.Fatalf("Usage: %s <image> <container>", os.Args[0])
	}

	imageName := os.Args[1]
	containerName := os.Args[2]

	if err := runContainer(imageName, containerName); err != nil {
		log.Fatalf("Error: %s", err)
	}
}

func runContainer(imageName, containerName string) error {
	client, err := containerd.New("/run/containerd/containerd.sock")
	if err != nil {
		return fmt.Errorf("failed to connect to containerd: %w", err)
	}
	defer client.Close()

	ctx := namespaces.WithNamespace(context.Background(), "default")

	image, err := client.Pull(ctx, imageName, containerd.WithPullUnpack)
	if err != nil {
		return fmt.Errorf("failed to pull image: %w", err)
	}

	container, err := client.NewContainer(
		ctx,
		containerName,
		containerd.WithNewSnapshot(containerName+"-snapshot", image),
		containerd.WithNewSpec(oci.WithImageConfig(image)),
	)
	if err != nil {
		return fmt.Errorf("failed to create container: %w", err)
	}
	defer container.Delete(ctx, containerd.WithSnapshotCleanup)

	task, err := container.NewTask(ctx, cio.NewCreator())
	if err != nil {
		return fmt.Errorf("failed to create task: %w", err)
	}
	defer task.Delete(ctx)

	if err := task.Start(ctx); err != nil {
		return fmt.Errorf("failed to start container: %w", err)
	}

	fmt.Printf("Container '%s' is running (PID: %d)\n", containerName, task.Pid())
	return nil
}

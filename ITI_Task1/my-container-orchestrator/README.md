# Containerd Utility

This project is a simple Go utility that uses containerd's API to pull a Docker image, create a container with a new snapshot, configure an OCI runtime spec (using the image configuration and host network namespace), and start the container as a running task. This allows you to run containers (for example, an Nginx container) directly via Go code.

## Features

- **Image Pulling:** Automatically pulls the specified Docker image from a registry.
- **Snapshot Creation:** Creates a new read-write snapshot for the container.
- **OCI Spec Configuration:** Generates a new OCI runtime specification based on the image, including setting the container to use the host network.
- **Task Launch:** Starts the container as a task and prints the container's process ID (PID).

## Prerequisites

- **Go:** Version 1.18 or higher is recommended.
- **containerd:** Must be installed and running on your system.
- **Permissions:** Ensure you have the necessary permissions to access `/run/containerd/containerd.sock`. Running the utility with `sudo` is common.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd my-container-orchestrator
   ```

2. **Initialize the Go Module (if not already done):**
   ```sh
   go mod init my-container-orchestrator
   go mod tidy
   ```

## Usage

Run the utility using the following command syntax:
```sh
sudo go run main.go <image-name> <container-name>
```

For example, to run an Nginx container:
```sh
sudo go run main.go docker.io/library/nginx:latest my-nginx-container
```

### Expected Output

After running the command, you should see an output similar to:
```
Container 'my-nginx-container' is running (PID: 12345)
```
Since the container is using the host network namespace, you can access the running Nginx server via:
```sh
curl http://localhost
```

## Code Overview

- **main.go:**  
  - Parses command-line arguments for the image name and container name.
  - Connects to containerd using the socket at `/run/containerd/containerd.sock`.
  - Pulls the specified image with unpacking enabled.
  - Creates a new container with a snapshot (named `<container-name>-snapshot`) and generates an OCI spec that includes `oci.WithHostNamespace("network")` to use the host network.
  - Starts a new task (i.e., launches the container) and prints its PID.

## Cleanup

To stop and remove your containers and associated tasks, you can use containerd’s CLI tool `ctr`. For example, to remove a specific container:
```sh
sudo ctr tasks kill my-nginx-container
sudo ctr containers delete my-nginx-container
```

Or remove all containers:
```sh
for container in $(sudo ctr containers list -q); do
    sudo ctr tasks kill $container || true
    sudo ctr containers delete $container || true
done
```


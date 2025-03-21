# Text to PDF Converter Application

## Download the Raw file to start build the image

```bash
wget https://raw.githubusercontent.com/ziyad-tarek1/Docker_The_Hard_Way/refs/heads/main/Text-To-PDF/Containerfile
```

## Build Application Image from Dockerfile

```bash
docker image build -t myapp -f Containerfile .
```

## List Created Image

```bash
docker image ls
```

## Run a Container in the Background

1. Create directories for volume mounts:
   ```bash
   sudo mkdir -p /data/input
   sudo mkdir -p /data/output
   sudo chmod 777 /data/input
   sudo chmod 777 /data/output/
   ```


2. Start the container:
   ```bash
   docker container run -d --name myapp \
     -v /data/input:/data/input:Z \
     -v /data/output:/data/output:Z \
     myapp
   ```

## Verify Container Status

```bash
docker ps
```

## Create Systemd Service for the Container

1. Prepare the systemd user directory:
   ```bash
   mkdir -p ~/.config/systemd/user
   cd ~/.config/systemd/user
   ```

2. Generate the systemd unit file:
   ```bash
   docker generate systemd --name myapp --new --files
   ```

3. **Enable linger** (allows user services to start at boot):
   ```bash
   sudo loginctl enable-linger $USER  
   ```

4. **Verify linger is enabled**:
   ```bash
   loginctl show-user $USER | grep Linger
   ```
   Output should include `Linger=yes`.

5. Verify the service statue:
   ```bash
   systemctl --user status container-myapp.service
   ```
6. If the service is created correctly stop and remove the container **Note: This step is very important**  :
   ```bash
   docker stop myapp
   docker rm myapp
   ```
     
7. Enable and start the service:
   ```bash
   systemctl --user enable --now container-myapp.service
   systemctl --user status container-myapp.service
   ```
## Reboot and Check service Status

1. Reboot your system:
   ```bash
   sudo reboot
   ```

2. After reboot, verify the service is running:
   ```bash
   systemctl --user status container-myapp.service
   ```

## Test the Application

1. Create a test input file:
   ```bash
   echo "Sample text to be converted into a PDF" > /data/input/hello.txt
   ```

2. Check the output directory for the converted PDF:
   ```bash
   ls -lh /data/output
   ```

---

**Notes**:  
- Linger ensures user services persist after reboot. Use `sudo` if you lack permissions.  
- If `Linger=no` appears in the check, repeat Step 3 with admin privileges.  

**Happy coding! 🚀**

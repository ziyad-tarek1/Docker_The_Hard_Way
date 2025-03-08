### **LAB #1 - Docker Containers & cgroups**  

![image](https://github.com/user-attachments/assets/1670d804-677b-4d49-8ca0-5908754deef8)


#### **1️⃣ Pull `nginx:alpine` Image**  
```bash
docker pull nginx:alpine
```
![image](https://github.com/user-attachments/assets/5d3e0e1f-7cda-459a-a6ae-fc5431a2e350)


#### **2️⃣ Run `nginx:alpine` Container in Background**  
```bash
docker run -d --name ziyad-tarek-ITI-45 nginx:alpine
```
![image](https://github.com/user-attachments/assets/85676ab4-a820-4ad1-a6ad-4827a6364ea9)
  
---

#### **3️⃣ Run Apache Container with Resource Limits**  
```bash
docker run -d --name limited-container --memory=70m --cpus=1 httpd:alpine
```
![image](https://github.com/user-attachments/assets/d3070456-eaa8-4dfd-9027-dd152b8484bd)

---

#### **4️⃣ Get the Path of cgroups for Apache Container**  
First, get the **container ID** of the Apache container:  
```bash
docker ps | grep httpd
```
Then, use the container ID to find its **cgroup path** refer to the [DOC](https://docs.docker.com/engine/containers/runmetrics/):  

```bash
sudo ls -al /sys/fs/cgroup/system.slice/docker-6e1986f7bd30658e999ec5409cbf71b36c3acb24fddd49c096709bfdd2bdba8d.scope/
```
![image](https://github.com/user-attachments/assets/b8098528-9bd7-49d1-8d94-5834846f7bb9)

![image](https://github.com/user-attachments/assets/3cb93a62-d894-4048-882d-6a36b7f78619)

---

#### **5️⃣ Get `memory.max` of Apache Container**  
```bash
sudo cat /sys/fs/cgroup/system.slice/docker-6e1986f7bd30658e999ec5409cbf71b36c3acb24fddd49c096709bfdd2bdba8d.scope/memory.max
```
![image](https://github.com/user-attachments/assets/9294559c-d081-4469-b645-af34f2401a95)

This command will output the **memory limit (70MB) set for the Apache container**.



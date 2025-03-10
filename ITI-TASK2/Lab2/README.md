# Lab 2 - ITI Task 2


## **Step 1: Create a Docker Network**
Run the following command to create a new Docker network:
```sh
docker network create --driver bridge --subnet=10.0.0.0/8 iti-network
```
![image](https://github.com/user-attachments/assets/138034af-5bcd-4a5d-9941-bdcfa486fee5)

---

## **Step 2: Run the Nginx Container with Volume**
Run the following command to start the container:
```sh
docker run -d --name nginx-alpine-iti \
  --network iti-network \
  -p 8080:80 \
  -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
  nginx:alpine
```
![image](https://github.com/user-attachments/assets/a2e3857e-8c3e-4d53-9c81-6cc9c83ccfb6)

---

## **Step 3: Verify the Setup**
Check if the container is running:
```sh
docker ps
```
![image](https://github.com/user-attachments/assets/3d917911-4e3f-49f0-94ed-1ed9e05c4043)

Test the web page:
```sh
curl http://localhost:8080
```
![image](https://github.com/user-attachments/assets/05ba45fc-be5c-470f-b19f-7014659e7ca9)


---

## Run with Apache (httpd)**
To use `httpd` instead of `nginx`, run:
```sh
docker run -d --name nginx-alpine-iti \
  --network iti-network \
  -p 8080:80 \
  -v $(pwd)/index.html:/usr/local/apache2/htdocs/index.html \
  httpd
```


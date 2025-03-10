# Lab 2 - ITI Task 2


## **Step 1: Create a Docker Network**
Run the following command to create a new Docker network:
```sh
docker network create --driver bridge --subnet=10.0.0.0/8 iti-network
```

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

---

## **Step 3: Verify the Setup**
Check if the container is running:
```sh
docker ps
```

Test the web page:
```sh
curl http://localhost:8080
```


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


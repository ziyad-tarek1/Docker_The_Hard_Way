FROM nginx:alpine
COPY . /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
ENV NGINX_PORT=80
EXPOSE $NGINX_PORT
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
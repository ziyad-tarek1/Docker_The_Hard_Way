FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

ENV APP_NAME="MyApp"

EXPOSE 3000

CMD ["node", "server.js"]
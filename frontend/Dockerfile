# syntax=docker/dockerfile:1
FROM node:12.21.0-alpine
WORKDIR /frontend
COPY package*.json ./
RUN apk add --no-cache python g++ make
RUN npm install
COPY . /frontend/
EXPOSE 8080
CMD [ "npm", "run", "serve"]

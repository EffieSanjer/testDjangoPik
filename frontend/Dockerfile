FROM node:20

WORKDIR /app

COPY *.json ./
RUN npm install
COPY . .

RUN npm run build

CMD ["npm", "run", "start"]

FROM node:14

WORKDIR /app

ADD package.json /app/
RUN npm install

ADD . /app/

CMD ["npm", "start"]

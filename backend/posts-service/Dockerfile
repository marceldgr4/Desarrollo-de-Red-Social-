FROM node:18-alpine

WORKDIR /app


RUN apk add --no-cache openssl


COPY package*.json ./
COPY prisma ./prisma/


RUN npm install


COPY . .


RUN npx prisma generate


RUN npm run build


EXPOSE 3002


CMD ["sh", "-c", "npx prisma migrate resolve --applied 20240101000000_init || true && npx prisma migrate deploy && npm start"]

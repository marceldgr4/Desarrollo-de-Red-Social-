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

# Start command
CMD ["sh", "-c", "npx prisma db push --accept-data-loss && npm start"]

CREATE DATABASE social_network;

-- Tabla de Usuarios
CREATE TABLE "users" (
    "id" SERIAL NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- Tabla de Posts
CREATE TABLE "posts" (
    "id" SERIAL NOT NULL,
    "message" TEXT NOT NULL,
    "userId" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "posts_pkey" PRIMARY KEY ("id")
);

CREATE UNIQUE INDEX "users_username_key" ON "users"("username");
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

 -- CREAR RELACIONES (FOREIGN KEYS)
ALTER TABLE "posts" 
ADD CONSTRAINT "posts_userId_fkey" 
FOREIGN KEY ("userId") 
REFERENCES "users"("id") 
ON DELETE RESTRICT 
ON UPDATE CASCADE;

-- creacion de Usuario 1
INSERT INTO "users" ("username", "email", "password", "createdAt", "updatedAt")
VALUES (
    'user1',
    'user1@example.com',
    'password123', 
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

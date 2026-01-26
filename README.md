# 🌐 Social Network - Full Stack Application

Red social desarrollada con arquitectura de microservicios usando Node.js, Express, TypeScript, React y PostgreSQL.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Arquitectura](#arquitectura)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [API Documentation](#api-documentation)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Testing](#testing)

## ✨ Características

- ✅ Autenticación de usuarios con JWT
- ✅ Crear publicaciones
- ✅ Visualizar feed de publicaciones
- ✅ Arquitectura de microservicios
- ✅ TypeScript en Frontend y Backend
- ✅ Dockerización completa
- ✅ Documentación Swagger
- ✅ Seeder de datos de prueba
- ✅ Manejo de estado con Zustand
- ✅ ORM Prisma para PostgreSQL

## 🚀 Tecnologías Utilizadas

### Backend
- **Node.js** - Runtime de JavaScript
- **Express.js** - Framework web
- **TypeScript** - Tipado estático
- **Prisma** - ORM para PostgreSQL
- **JWT** - Autenticación
- **bcryptjs** - Encriptación de contraseñas
- **Swagger** - Documentación API

### Frontend
- **React 18** - Librería UI
- **TypeScript** - Tipado estático
- **Zustand** - Manejo de estado
- **Axios** - Cliente HTTP

### Base de Datos
- **PostgreSQL** - Base de datos relacional

### DevOps
- **Docker** - Contenedorización
- **Docker Compose** - Orquestación de contenedores

## 🏗️ Arquitectura

```
┌─────────────────┐
│    Frontend     │
│   React + TS    │
│   Port: 3000    │
└────────┬────────┘
         │
         ├──────────────────┬──────────────────┐
         │                  │                  │
┌────────▼────────┐  ┌──────▼────────┐  ┌────▼──────────┐
│  Auth Service   │  │ Posts Service │  │   PostgreSQL  │
│   Port: 3001    │  │  Port: 3002   │  │   Port: 5432  │
└─────────────────┘  └───────────────┘  └───────────────┘
```

## 📦 Requisitos Previos

- [Docker](https://docs.docker.com/get-docker/) (v20.10+)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2.0+)
- [Node.js](https://nodejs.org/) (v18+) - Solo para desarrollo local
- [npm](https://www.npmjs.com/) o [yarn](https://yarnpkg.com/) - Solo para desarrollo local

## 🔧 Instalación

### Opción 1: Usando Docker (Recomendado)

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd social-network-fullstack
```

2. **Levantar todos los servicios**
```bash
docker-compose up --build
```

Este comando:
- Construirá las imágenes Docker
- Iniciará PostgreSQL
- Ejecutará las migraciones de Prisma
- Creará usuarios de prueba
- Levantará los microservicios
- Iniciará el frontend

3. **Acceder a la aplicación**
- Frontend: http://localhost:3000
- Auth Service: http://localhost:3001
- Posts Service: http://localhost:3002
- Swagger Auth: http://localhost:3001/api-docs
- Swagger Posts: http://localhost:3002/api-docs

### Opción 2: Desarrollo Local

#### Backend - Auth Service

```bash
cd backend/auth-service
npm install
npm run prisma:generate
npm run prisma:migrate
npm run seed
npm run dev
```

#### Backend - Posts Service

```bash
cd backend/posts-service
npm install
npm run prisma:generate
npm run prisma:migrate
npm run dev
```

#### Frontend

```bash
cd frontend
npm install
npm start
```

## 🎯 Uso

### Credenciales de Prueba

El sistema incluye 5 usuarios de prueba:

| Usuario | Contraseña |
|---------|-----------|
| user1   | password123 |
| user2   | password123 |
| user3   | password123 |
| user4   | password123 |
| user5   | password123 |

### Flujo de Usuario

1. **Login**: Inicia sesión con cualquiera de las credenciales de prueba
2. **Ver Posts**: Automáticamente verás el feed con las publicaciones
3. **Crear Post**: Escribe un mensaje y presiona "Post"
4. **Logout**: Cierra sesión desde el botón en el header

## 📚 API Documentation

### Auth Service (Port 3001)

#### POST /api/auth/login
Autentica un usuario y retorna un token JWT.

**Request Body:**
```json
{
  "username": "user1",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com"
  }
}
```

### Posts Service (Port 3002)

#### GET /api/posts
Obtiene todas las publicaciones.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
[
  {
    "id": 1,
    "message": "Hello! This is my first post...",
    "createdAt": "2024-01-26T10:00:00.000Z",
    "user": {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com"
    }
  }
]
```

#### POST /api/posts
Crea una nueva publicación.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "message": "This is my new post!"
}
```

**Response:**
```json
{
  "message": "Post created successfully",
  "post": {
    "id": 6,
    "message": "This is my new post!",
    "userId": 1,
    "createdAt": "2024-01-26T10:30:00.000Z",
    "user": {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com"
    }
  }
}
```

## 📁 Estructura del Proyecto

```
social-network-fullstack/
├── backend/
│   ├── auth-service/
│   │   ├── prisma/
│   │   │   ├── schema.prisma
│   │   │   └── migrations/
│   │   ├── src/
│   │   │   ├── controllers/
│   │   │   │   └── auth.controller.ts
│   │   │   ├── routes/
│   │   │   │   └── auth.routes.ts
│   │   │   ├── index.ts
│   │   │   └── seed.ts
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   └── posts-service/
│       ├── prisma/
│       │   ├── schema.prisma
│       │   └── migrations/
│       ├── src/
│       │   ├── controllers/
│       │   │   └── posts.controller.ts
│       │   ├── middleware/
│       │   │   └── auth.middleware.ts
│       │   ├── routes/
│       │   │   └── posts.routes.ts
│       │   └── index.ts
│       ├── Dockerfile
│       ├── package.json
│       └── tsconfig.json
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.tsx
│   │   │   ├── PostsList.tsx
│   │   │   └── CreatePost.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── store/
│   │   │   └── authStore.ts
│   │   ├── App.tsx
│   │   ├── App.css
│   │   └── index.tsx
│   ├── Dockerfile
│   ├── package.json
│   └── tsconfig.json
│
├── database/
│   └── init.sql
│
├── docker-compose.yml
└── README.md
```

## 🧪 Testing

### Ejecutar Tests

```bash
# Auth Service
cd backend/auth-service
npm test

# Posts Service
cd backend/posts-service
npm test

# Frontend
cd frontend
npm test
```

## 🛠️ Comandos Útiles

### Docker

```bash
# Levantar servicios
docker-compose up

# Levantar en background
docker-compose up -d

# Reconstruir imágenes
docker-compose up --build

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down

# Limpiar volúmenes (elimina datos)
docker-compose down -v
```

### Prisma

```bash
# Generar cliente Prisma
npm run prisma:generate

# Ejecutar migraciones
npm run prisma:migrate

# Resetear base de datos
npx prisma migrate reset

# Ver base de datos
npx prisma studio
```

## 🔐 Variables de Entorno

### Auth Service (.env)
```env
DATABASE_URL="postgresql://postgres:postgres123@postgres:5432/social_network"
JWT_SECRET="mi_secreto_super_seguro_2024"
PORT=3001
```

### Posts Service (.env)
```env
DATABASE_URL="postgresql://postgres:postgres123@postgres:5432/social_network"
JWT_SECRET="mi_secreto_super_seguro_2024"
PORT=3002
```

### Frontend (.env)
```env
REACT_APP_AUTH_SERVICE_URL=http://localhost:3001
REACT_APP_POSTS_SERVICE_URL=http://localhost:3002
```

## 📝 Notas Importantes

1. **Primera ejecución**: La primera vez que ejecutes `docker-compose up` puede tardar varios minutos mientras se descargan las imágenes y se construyen los contenedores.

2. **Seeders**: Los usuarios de prueba se crean automáticamente al iniciar el auth-service.

3. **JWT Secret**: En producción, asegúrate de usar un secreto fuerte y único.

4. **CORS**: Los servicios están configurados para aceptar requests desde cualquier origen en desarrollo. En producción, limita los orígenes permitidos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto fue desarrollado como prueba técnica.

## 👨‍💻 Autor

Desarrollado como parte de una prueba técnica Full Stack.

## 📞 Soporte

Para preguntas o problemas, por favor abre un issue en el repositorio.

---

⭐ Si te gustó este proyecto, dale una estrella en GitHub!

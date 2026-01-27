-- inicialización de la base de datos para la red social
-- se ejecutará automáticamente al iniciar el contenedor PostgreSQL.

-- Crear la base de datos si no existe 
-- (gestionado por variables de entorno de Docker).

-- Las tablas se crearán mediante migraciones de Prisma.
-- Este archivo se puede utilizar para configurar la base de datos si es necesario.

--Crear extensiones si es necesario

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";



import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import swaggerUi from 'swagger-ui-express';
import swaggerJsdoc from 'swagger-jsdoc';
import postRoutes from './routes/posts.routes';

dotenv.config();

const app = express();
const PORT = Number(process.env.PORT) || 3002;

// CORS Configuration - Allow requests from frontend
app.use(cors({
  origin: ['http://localhost:3000', 'http://127.0.0.1:3000', 'http://localhost:3002'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'Accept'],
}));
app.use(express.json());


const swaggerOptions = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Posts Service API',
      version: '1.0.0',
      description: 'Posts microservice for social network',
    },
    servers: [
      {
        url: `http://localhost:${PORT}`,
        description: 'Development server',
      },
    ],
    components: {
      securitySchemes: {
        bearerAuth: {
          type: 'http',
          scheme: 'bearer',
          bearerFormat: 'JWT',
        },
      },
    },
  },
  apis: ['./src/routes/*.ts'],
};

const swaggerSpec = swaggerJsdoc(swaggerOptions);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));


app.use('/api/posts', postRoutes);


app.get('/health', (req, res) => {
  res.json({ status: 'OK', service: 'posts-service' });
});


app.listen(PORT, '0.0.0.0', () => {
  console.log(` Posts Service running on port ${PORT}`);
  console.log(` Swagger documentation available at http://localhost:${PORT}/api-docs`);
  console.log(` Server listening on 0.0.0.0:${PORT} (accessible via Docker port mapping)`);
});

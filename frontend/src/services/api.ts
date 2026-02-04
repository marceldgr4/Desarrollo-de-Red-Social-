import axios from 'axios';
import { useAuthStore } from '../store/authStore';

const AUTH_SERVICE_URL = process.env.REACT_APP_AUTH_SERVICE_URL || 'http://localhost:3001';
const POSTS_SERVICE_URL = process.env.REACT_APP_POSTS_SERVICE_URL || 'http://localhost:3002';

// Create axios instances
const authService = axios.create({ baseURL: AUTH_SERVICE_URL });
const postsService = axios.create({ baseURL: POSTS_SERVICE_URL });

// Add interceptor to handle 401 errors
const handleUnauthorized = (error: any) => {
  if (error.response && error.response.status === 401) {
    useAuthStore.getState().logout();
  }
  return Promise.reject(error);
};

authService.interceptors.response.use((response) => response, handleUnauthorized);
postsService.interceptors.response.use((response) => response, handleUnauthorized);

// Auth Service API
export const authAPI = {
  login: async (username: string, password: string) => {
    const response = await authService.post('/api/auth/login', {
      username,
      password,
    });
    return response.data;
  },
};

// Posts Service API
export const postsAPI = {
  getPosts: async (token: string) => {
    const response = await postsService.get('/api/posts', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  },

  createPost: async (token: string, message: string) => {
    const response = await postsService.post(
      '/api/posts',
      { message },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  },
  updatePost: async (token: string, postId: number, message: string) => {
    const response = await postsService.put(
      `/api/posts/${postId}`,
      { message },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  },

  deletePost: async (token: string, postId: number) => {
    const response = await postsService.delete(
      `/api/posts/${postId}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  },
};

import axios from 'axios';

const AUTH_SERVICE_URL = process.env.REACT_APP_AUTH_SERVICE_URL || 'http://localhost:3001';
const POSTS_SERVICE_URL = process.env.REACT_APP_POSTS_SERVICE_URL || 'http://localhost:3002';

// Auth Service API
export const authAPI = {
  login: async (username: string, password: string) => {
    const response = await axios.post(`${AUTH_SERVICE_URL}/api/auth/login`, {
      username,
      password,
    });
    return response.data;
  },
};

// Posts Service API
export const postsAPI = {
  getPosts: async (token: string) => {
    const response = await axios.get(`${POSTS_SERVICE_URL}/api/posts`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  },

  createPost: async (token: string, message: string) => {
    const response = await axios.post(
      `${POSTS_SERVICE_URL}/api/posts`,
      { message },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  },
};

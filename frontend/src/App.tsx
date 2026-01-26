import React, { useEffect } from 'react';
import Login from './components/Login';
import PostsList from './components/PostsList';
import CreatePost from './components/CreatePost';
import { useAuthStore } from './store/authStore';
import './App.css';

const App: React.FC = () => {
  const { token, logout, user } = useAuthStore();

  useEffect(() => {
    // Check if token exists in localStorage on mount
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      useAuthStore.getState().setToken(storedToken);
    }
  }, []);

  if (!token) {
    return <Login />;
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="container">
          <h1>🌐 Social Network</h1>
          <div className="user-info">
            <span>Welcome, <strong>{user?.username}</strong>!</span>
            <button onClick={logout} className="btn btn-secondary">
              Logout
            </button>
          </div>
        </div>
      </header>

      <main className="container">
        <div className="main-content">
          <CreatePost />
          <PostsList />
        </div>
      </main>

      <footer className="app-footer">
        <p>© 2024 Social Network - Full Stack Technical Test</p>
      </footer>
    </div>
  );
};

export default App;

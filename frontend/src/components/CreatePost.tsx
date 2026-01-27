import React, { useState } from 'react';
import { postsAPI } from '../services/api';
import { useAuthStore } from '../store/authStore';

const CreatePost: React.FC = () => {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const { token } = useAuthStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!message.trim()) {
      setError('Please enter a message');
      return;
    }

    if (!token) {
      setError('You must be logged in to post');
      return;
    }

    setLoading(true);
    setError('');
    setSuccess(false);

    try {
      await postsAPI.createPost(token, message);
      setMessage('');
      setSuccess(true);
      
      // Refresh posts list
      if ((window as any).refreshPosts) {
        (window as any).refreshPosts();
      }

      // Hide success message after 3 seconds
      setTimeout(() => setSuccess(false), 3000);
    } catch (err: any) {
      setError(
        err.response?.data?.error || 'Failed to create post. Please try again.'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2> Crear Post</h2>
      <form onSubmit={handleSubmit}>
        {error && <div className="error-message">{error}</div>}
        {success && (
          <div className="success-message">
            Post creado exitosamente! 
          </div>
        )}

        <div className="form-group">
          <label htmlFor="message">¿Qué hay en tu mente?</label>
          <textarea
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Comparte tus pensamientos..."
            required
            maxLength={500}
          />
          <small style={{ color: '#999', fontSize: '0.9rem' }}>
            {message.length}/500 caracteres
          </small>
        </div>

        <button
          type="submit"
          className="btn btn-primary"
          disabled={loading || !message.trim()}
        >
          {loading ? 'Publicando...' : 'Publicar'}
        </button>
      </form>
    </div>
  );
};

export default CreatePost;

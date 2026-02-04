import React, { useEffect, useState } from 'react';
import { postsAPI } from '../services/api';
import { useAuthStore } from '../store/authStore';

interface Post {
  id: number;
  message: string;
  createdAt: string;
  user: {
    id: number;
    username: string;
    email: string;
  };
}

const PostsList: React.FC = () => {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { token, user } = useAuthStore();

  const fetchPosts = async () => {
    if (!token) return;

    try {
      setLoading(true);
      setError('');
      const data = await postsAPI.getPosts(token);
      setPosts(data);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to load posts');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = async (postId: number) => {
    const postToEdit = posts.find((p) => p.id === postId);
    if (!postToEdit) return;

    const newMessage = window.prompt('Editar post:', postToEdit.message);
    if (newMessage === null || newMessage === postToEdit.message) return;

    try {
      if (token) {
        await postsAPI.updatePost(token, postId, newMessage);
        // Refresh posts after update
        fetchPosts();
      }
    } catch (err) {
      alert('Error updating post');
      console.error(err);
    }
  };

  const handleDelete = async (postId: number) => {
    const confirmed = window.confirm('¿Estás seguro de que quieres eliminar este post?');
    if (!confirmed) return;

    try {
      if (token) {
        await postsAPI.deletePost(token, postId);
        // Refresh posts after delete
        fetchPosts();
      }
    } catch (err) {
      alert('Error deleting post');
      console.error(err);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, [token]);

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };


  const refreshPosts = () => {
    fetchPosts();
  };

  React.useEffect(() => {
    (window as any).refreshPosts = refreshPosts;
    return () => {
      delete (window as any).refreshPosts;
    };
  }, [token]);

  if (loading) {
    return (
      <div className="card">
        <div className="loading">Cargando posts...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <div className="error-message">{error}</div>
        <button onClick={fetchPosts} className="btn btn-primary">
          Intentar de nuevo
        </button>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Feed</h2>
      {posts.length === 0 ? (
        <div className="empty-state">
          <div className="empty-state-icon"></div>
          <p>No hay posts aun. Ser el primero en publicar algo!</p>
        </div>
      ) : (
        <div className="posts-list">
          {posts.map((post) => (
            <div key={post.id} className="post-card">
              <div className="post-header">
                <div className="post-author">@{post.user.username}</div>
                <div className="post-date">{formatDate(post.createdAt)}</div>
              </div>

              <div className="post-message">{post.message}</div>

              {user && user.id === post.user.id && (
                <div className="post-actions">
                  <button onClick={() => handleEdit(post.id)} className="btn btn-secondary">
                    Editar
                  </button>
                  <button onClick={() => handleDelete(post.id)} className="btn btn-danger">
                    Eliminar
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default PostsList;

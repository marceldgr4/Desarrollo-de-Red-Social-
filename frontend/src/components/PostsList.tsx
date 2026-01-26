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
  const { token } = useAuthStore();

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

  // Function to be called when a new post is created
  const refreshPosts = () => {
    fetchPosts();
  };

  // Expose refresh function to parent
  React.useEffect(() => {
    (window as any).refreshPosts = refreshPosts;
    return () => {
      delete (window as any).refreshPosts;
    };
  }, [token]);

  if (loading) {
    return (
      <div className="card">
        <div className="loading">Loading posts...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <div className="error-message">{error}</div>
        <button onClick={fetchPosts} className="btn btn-primary">
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>📱 Feed</h2>
      {posts.length === 0 ? (
        <div className="empty-state">
          <div className="empty-state-icon">📭</div>
          <p>No posts yet. Be the first to post something!</p>
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
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default PostsList;

import { Response } from 'express';
import { PrismaClient } from '@prisma/client';
import { AuthRequest } from '../middleware/auth.middleware';

const prisma = new PrismaClient();

export const getPosts = async (req: AuthRequest, res: Response): Promise<void> => {
  try {
    const posts = await prisma.post.findMany({
      include: {
        user: {
          select: {
            id: true,
            username: true,
            email: true,
          },
        },
      },
      orderBy: {
        createdAt: 'desc',
      },
    });

    res.json(posts);
  } catch (error) {
    console.error('Get posts error:', error);
    res.status(500).json({
      error: 'Internal server error'
    });
  }
};

export const createPost = async (req: AuthRequest, res: Response): Promise<void> => {
  try {
    const { message } = req.body;
    const userId = req.user?.userId;

    // Validate input
    if (!message) {
      res.status(400).json({
        error: 'Message is required'
      });
      return;
    }

    if (!userId) {
      res.status(401).json({
        error: 'User not authenticated'
      });
      return;
    }

    // Create post
    const post = await prisma.post.create({
      data: {
        message,
        userId,
      },
      include: {
        user: {
          select: {
            id: true,
            username: true,
            email: true,
          },
        },
      },
    });

    res.status(201).json({
      message: 'Post created successfully',
      post,
    });
  } catch (error) {
    console.error('Create post error:', error);
    res.status(500).json({
      error: 'Internal server error'
    });
  }
};
export const updatePost = async (req: AuthRequest, res: Response): Promise<void> => {
  try {
    const { message } = req.body;
    const userId = req.user?.userId;
    const postId = req.params.postId;

    // Validate input
    if (!message) {
      res.status(400).json({
        error: 'Message is required'
      });
      return;
    }

    if (!userId) {
      res.status(401).json({
        error: 'User not authenticated'
      });
      return;
    }

    // Check if post exists and user owns it
    const existingPost = await prisma.post.findUnique({
      where: {
        id: Number(postId),
      },
    });

    if (!existingPost) {
      res.status(404).json({
        error: 'Post not found'
      });
      return;
    }

    if (existingPost.userId !== userId) {
      res.status(403).json({
        error: 'You are not authorized to edit this post'
      });
      return;
    }

    // Update post
    const post = await prisma.post.update({
      where: {
        id: Number(postId),
      },
      data: {
        message,
      },
      include: {
        user: {
          select: {
            id: true,
            username: true,
            email: true,
          },
        },
      },
    });

    res.status(200).json({
      message: 'Post updated successfully',
      post,
    });
  } catch (error) {
    console.error('Update post error:', error);
    res.status(500).json({
      error: 'Internal server error'
    });
  }
};

export const deletePost = async (req: AuthRequest, res: Response): Promise<void> => {
  try {
    const userId = req.user?.userId;
    const postId = req.params.postId;

    if (!userId) {
      res.status(401).json({
        error: 'User not authenticated'
      });
      return;
    }

    // Check if post exists and user owns it
    const existingPost = await prisma.post.findUnique({
      where: {
        id: Number(postId),
      },
    });

    if (!existingPost) {
      res.status(404).json({
        error: 'Post not found'
      });
      return;
    }

    if (existingPost.userId !== userId) {
      res.status(403).json({
        error: 'You are not authorized to delete this post'
      });
      return;
    }

    // Delete post
    await prisma.post.delete({
      where: {
        id: Number(postId),
      },
    });

    res.status(200).json({
      message: 'Post deleted successfully'
    });
  } catch (error) {
    console.error('Delete post error:', error);
    res.status(500).json({
      error: 'Internal server error'
    });
  }
};
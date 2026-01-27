import { PrismaClient } from '@prisma/client';
import bcrypt from 'bcryptjs';

const prisma = new PrismaClient();

async function main() {
  console.log('Starting seed...');

  
  const users = [
    {
      username: 'user1',
      email: 'user1@example.com',
      password: await bcrypt.hash('password123', 10),
    },
    {
      username: 'user2',
      email: 'user2@example.com',
      password: await bcrypt.hash('password123', 10),
    },
    {
      username: 'user3',
      email: 'user3@example.com',
      password: await bcrypt.hash('password123', 10),
    },
  
  ];

  const existingUsers = await prisma.user.findMany();
  
  if (existingUsers.length > 0) {
    console.log(' Users already seeded, skipping...');
    return;
  }

 
  for (const userData of users) {
    await prisma.user.create({
      data: {
        ...userData,
        posts: {
          create: {
            message: `Hello! This is my first post from ${userData.username}. Excited to be part of this social network! 🎉`,
          },
        },
      },
    });
  }

  console.log(' Seed completed successfully!');
  console.log(`Created ${users.length} users with initial posts`);
  console.log('\nTest credentials:');
  console.log('Username: user1 | Password: password123');
 
}

main()
  .catch((e) => {
    console.error(' -X- Seed error:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

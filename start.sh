#!/bin/bash

echo "🚀 Starting Social Network Application..."
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Stop any existing containers
echo "🛑 Stopping any existing containers..."
docker-compose down

echo ""
echo "🏗️  Building and starting all services..."
echo "This may take a few minutes on first run..."
echo ""

# Build and start all services
docker-compose up --build -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "🎉 Application is ready!"
echo ""
echo "📍 Access the application at:"
echo "   Frontend:      http://localhost:3000"
echo "   Auth Service:  http://localhost:3001"
echo "   Posts Service: http://localhost:3002"
echo "   Swagger Auth:  http://localhost:3001/api-docs"
echo "   Swagger Posts: http://localhost:3002/api-docs"
echo ""
echo "🔐 Test Credentials:"
echo "   Username: user1"
echo "   Password: password123"
echo ""
echo "📋 View logs: docker-compose logs -f"
echo "🛑 Stop app:  docker-compose down"
echo ""

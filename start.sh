#!/bin/bash

echo "Starting the Social Network application"
echo ""

# Check Docker installation
if ! command -v docker >/dev/null 2>&1; then
    echo "Docker is not installed."
    echo "Please install Docker before running this script."
    exit 1
fi

# Check Docker Compose installation
if ! command -v docker-compose >/dev/null 2>&1; then
    echo "Docker Compose is not installed."
    echo "Please install Docker Compose before running this script."
    exit 1
fi

echo "Docker and Docker Compose are available."
echo ""

# Stop running containers if they exist
echo "Stopping existing containers..."
docker-compose down

echo ""
echo "Building and starting the services."
echo "This may take a few minutes the first time."
echo ""

# Start services
docker-compose up --build -d

echo ""
echo "Waiting for services to start..."
sleep 10

echo ""
echo "Application started successfully."
echo ""
echo "Services available at:"
echo "  Frontend:      http://localhost:3000"
echo "  Auth Service:  http://localhost:3001"
echo "  Posts Service: http://localhost:3002"
echo "  Swagger Auth:  http://localhost:3001/api-docs"
echo "  Swagger Posts: http://localhost:3002/api-docs"
echo ""
echo "Test user:"
echo "  Username: user1"
echo "  Password: password123"
echo ""
echo "Helpful commands:"
echo "  docker-compose logs -f"
echo "  docker-compose down"
echo ""

Flask Microservices with Docker

This project implements a User Service and an Order Service using Flask, MySQL, and Docker.

🚀 Getting Started

Prerequisites

Ensure you have the following installed:

Docker

Git

cURL or Postman for API testing

📌 Setup and Run

1️⃣ Clone the Repository

git clone <your-repo-url>
cd flask_microservices

2️⃣ Build and Start Containers

docker-compose up --build

3️⃣ Check Running Containers

docker ps

4️⃣ Verify Services

Once running, test the endpoints:

User Service: http://localhost:5001

Order Service: http://localhost:5002

📌 API Documentation

🛠 User Service (http://localhost:5001)

Method

Endpoint

Description

GET

/users

Get all users

POST

/register

Register a new user

Example: Register a New User

curl -X POST http://localhost:5001/register \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "password": "123456"}'

📦 Order Service (http://localhost:5002)

Method

Endpoint

Description

GET

/orders

Get all orders

POST

/orders

Create a new order

Example: Create an Order

curl -X POST http://localhost:5002/orders \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "product": "Laptop", "quantity": 2}'

📌 Stopping the Services

To stop running containers, press Ctrl + C or run:

docker-compose down

📌 Database Persistence

The database uses a Docker volume (mysql_data) to persist data. To verify:

docker volume ls

📌 Pushing to GitHub

git add .
git commit -m "Initial commit"
git push origin main

📌 Future Improvements

🔐 Add JWT authentication

📊 Implement Swagger UI for API documentation

🚀 Deploy to the cloud (AWS, DigitalOcean, Heroku)


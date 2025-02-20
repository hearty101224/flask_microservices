# 📌 API Documentation

## 🛠 User Service
### **Base URL:** `http://localhost:5001`

| Method | Endpoint        | Description            | Request Body |
|--------|---------------|----------------------|--------------|
| GET    | `/users`      | Get all users        | None         |
| POST   | `/users`      | Create a new user    | JSON        |
| GET    | `/users/{id}` | Get user by ID       | None         |
| PUT    | `/users/{id}` | Update user by ID    | JSON        |
| DELETE | `/users/{id}` | Delete user by ID    | None         |

---

## 📦 Order Service
### **Base URL:** `http://localhost:5002`

| Method | Endpoint        | Description           | Request Body |
|--------|---------------|---------------------|--------------|
| GET    | `/orders`     | Get all orders      | None         |
| POST   | `/orders`     | Create new order    | JSON        |
| GET    | `/orders/{id}` | Get order by ID     | None         |
| PUT    | `/orders/{id}` | Update order by ID  | JSON        |
| DELETE | `/orders/{id}` | Delete order by ID  | None         |

---

## 📌 Example Requests & Responses

### **1️⃣ Create a New Order (`POST /orders`)**
#### **📌 Request (cURL)**
```sh
curl -X POST http://localhost:5002/orders \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "product": "Laptop", "quantity": 2}'

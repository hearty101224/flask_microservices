from flask import Flask, request, jsonify
import mysql.connector
import requests
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "microservices_db")
    )

# Place Order
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    # Check if user exists (calling User Service API)
    user_response = requests.get('http://user_service:5001/users')  
    users = user_response.json()
    user_ids = [user[0] for user in users]

    if data['user_id'] not in user_ids:
        return jsonify({"error": "User not found"}), 404

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO orders (user_id, product_name, quantity) VALUES (%s, %s, %s)",
                   (data['user_id'], data['product_name'], data['quantity']))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Order placed successfully"}), 201

# Get Orders
@app.route('/orders', methods=['GET'])
def get_orders():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

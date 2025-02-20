from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os, requests

app = Flask(__name__)
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user_service:5001")

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:{os.getenv('DB_PASSWORD', 'root')}@{os.getenv('DB_HOST', 'db')}/{os.getenv('DB_NAME', 'microservices_db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    if not all([data.get("user_id"), data.get("product"), data.get("quantity")]):
        return jsonify({"error": "Missing required fields"}), 400

    user_response = requests.get(f"{USER_SERVICE_URL}/users")
    if user_response.status_code != 200:
        return jsonify({"error": "User service unavailable"}), 500

    users = user_response.json()
    if not any(u["id"] == data["user_id"] for u in users):
        return jsonify({"error": "User not found"}), 404

    new_order = Order(user_id=data["user_id"], product_name=data["product"], quantity=data["quantity"])
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully", "order_id": new_order.id}), 201


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        "id": order.id,
        "user_id": order.user_id,
        "product_name": order.product_name,
        "quantity": order.quantity
    } for order in orders])


if __name__ == '__main__':
    with app.app_context():  # ✅ Ensure create_all runs inside context
        db.create_all()
    app.run(host='0.0.0.0', port=5002, debug=True)

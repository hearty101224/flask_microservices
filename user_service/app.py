from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:{os.getenv('DB_PASSWORD', 'root')}@{os.getenv('DB_HOST', 'db')}/{os.getenv('DB_NAME', 'microservices_db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not all([data.get('name'), data.get('email'), data.get('password')]):
        return jsonify({"error": "Missing required fields"}), 400
    
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{ "id": u.id, "name": u.name, "email": u.email } for u in users])

if __name__ == '__main__':
    with app.app_context():  # ✅ Ensure create_all runs inside context
        db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)

from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "microservices_db")
    )

# Register User
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                   (data['name'], data['email'], data['password']))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "User registered successfully"}), 201

# Get Users
@app.route('/users', methods=['GET'])
def get_users():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

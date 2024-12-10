from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from models import db
from routes.librarian import librarian_blueprint
from routes.user import user_blueprint

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize Extensions
db.init_app(app)
jwt = JWTManager(app)
swagger = Swagger(app)

# Register Blueprints
app.register_blueprint(librarian_blueprint, url_prefix='/librarian')
app.register_blueprint(user_blueprint, url_prefix='/user')

# Add a route for the root URL ("/")
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System API!"}), 200

# Create Database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

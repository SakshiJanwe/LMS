from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Book, BorrowRequest

librarian_blueprint = Blueprint('librarian', __name__)

@librarian_blueprint.route('/create_user', methods=['POST'])
@jwt_required()
def create_user():
    current_user = get_jwt_identity()
    data = request.json
    new_user = User(email=data['email'], password=data['password'], role='user')
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

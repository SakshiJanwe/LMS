from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Book, BorrowRequest

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author} for book in books]), 200

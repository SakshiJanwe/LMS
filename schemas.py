from flask_marshmallow import Marshmallow
from models import User, Book, BorrowRequest

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

class BorrowRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BorrowRequest
        load_instance = True

from rest_framework import serializers

from books.models import BookReview, Book
from users.models import CustomUser


class BookSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", 'describtion', "isbn")

class UserSeralizier(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "email")

class BookReviewDetailSerializer(serializers.ModelSerializer):
    book = BookSerialazer()
    user = UserSeralizier()
    class Meta:
        model=BookReview
        fields=("stars_given", "comment", "book", "user")

from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import CustomUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    describtion = models.TextField()
    isbn = models.CharField(max_length=17)
    cover_picture = models.ImageField(default='default_cover.jpg')
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    bie = models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}".title()

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.book.title} {self.author.first_name} {self.author.last_name}"
class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username


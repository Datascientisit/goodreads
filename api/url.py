from django.urls import path
from api.views import BookReviewDetailApiView, BookListApiView
from users.user_url import app_name

app_name = "api"
urlpatterns = [
    path("reviews/", BookListApiView.as_view(), name = "review-list" ),
    path("reviews/<int:id>/", BookReviewDetailApiView.as_view(), name="review-detail")
]
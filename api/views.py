from django.core.serializers import serialize
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.seralizers import BookReviewDetailSerializer
from books.models import BookReview


class BookReviewDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializ = BookReviewDetailSerializer(book_review)
        return Response(data=serializ.data)

class BookListApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serialize = BookReviewDetailSerializer(page_obj, many=True)
        return paginator.get_paginated_response(serialize.data)
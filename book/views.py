from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Book
from .serializers import BookSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"

    @action(detail=True, methods=['GET'])
    def authors(self, request, pk=None):
        book = self.get_object()
        return Response({"author": book.author})
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(["GET", "POST"])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        my_serializer = BookSerializer(books, many=True)
        return Response(my_serializer.data)
    if request.method == "POST":
        my_serializer = BookSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=201)
        return Response(my_serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "DELETE":
        book.delete()
        return Response(status=204)
from django.urls import path

from .views import books_list, book_detail


urlpatterns = [
    path("", books_list, name="books_list"),
    path("<int:pk>/", book_detail, name="book_detail")
]
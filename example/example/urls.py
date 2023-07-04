from django.urls import path, include
from .views import helloAPI, booksAPI, bookAPI, BookAPIMixin, BooksAPIMixins

urlpatterns = [
    path("hello/", helloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixin.as_view()),

    
]

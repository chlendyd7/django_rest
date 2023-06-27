from django.urls import path, include
from .views import helloAPI, booksAPI, bookAPI

urlpatterns = [
    path("hello/", helloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),

    
]

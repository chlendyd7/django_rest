from rest_framework import serializers
from .models import Book
from django.db.models.fields import TextField

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description',]

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Book


class BooksSerializer(ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ['name', 'author']

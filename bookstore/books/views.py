from rest_framework.generics import ListAPIView

from .models import Book
from .serializers import BooksSerializer


class BooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

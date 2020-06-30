from django.urls import path

from .views import BooksView

urlpatterns = [
    path('', BooksView.as_view())
]

from django.urls import include, path

urlpatterns = [
    path('books/', include('bookstore.books.endpoints'))
]

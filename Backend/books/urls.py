from django.urls import path
from .views import *

urlpatterns = [
    path('books/create', upload_book, name='create_book'),
    path('books/details/<str:title>', details_book, name='details_book'),
    path('books/publisher/<str:publisher>', books_by_publisher, name='books_by_publisher'),
    path('books/author/<str:author>', books_by_author, name='books_by_author'),
    path('books/new_release', new_release_books, name='new_release_books'),
    path('books/new_arival', new_arival_books, name='new_arival'),
    path('books/donated', donate_book, name='donated_book'),
    path('books/borrowed', borrow_book, name='borrow_book'),
    path('books/returned', returned_book, name='return_book'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('books/create', upload_book, name='create_book'),
    # path('books/details/<str:title>', details_book, name='details_book'),
    # path('books/publisher/<str:publisher>', books_by_publisher, name='books_by_publisher'),
    path('books/author/<str:author>', books_by_author, name='books_by_author'),
    path('books/new_release', new_release_books, name='new_release_books'),
    path('books/new_arival', new_arival_books, name='new_arival'),
    path('books/donated', donate_book, name='donated_book'),
    path('books/borrowed', borrow_book, name='borrow_book'),
    # path('books/returned', returned_book, name='return_book'),
    path('books/bought', book_bought, name='bought_book'),
    path('books/get-byid', get_books, name='get_book'),
    path('books/list', list_books, name='list_books'),
    path('books/borrowed-list', list_books_borrowed, name='list_books_borrowed'),
    path('books/owned-list', list_books_owned, name='list_books_borrowed'),
    path('books/returned', returned_book, name='return_books'),
    path('books/genre',search_by_genre, name='search_by_genre'),
]
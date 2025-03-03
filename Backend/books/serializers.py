from .models import Book, BookDonated, BookBorrowed
from rest_framework import serializers
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','publication_date','release_date','description','price','publisher','genre']

class BookDonatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDonated
        fields = ['book','number_of_donated']

class BookBorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBorrowed
        fields = ['book', 'borrower_name']
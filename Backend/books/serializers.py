from .models import Book, BookDonated, BookBorrowed, BookOwned
from rest_framework import serializers
import datetime
import json

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','publication_date','release_date','description','price','publisher','isbn','genre','cover']

# class BookDonatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookDonated
#         fields = ['book','number_of_donated']

# class BookBorrowedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookBorrowed
#         fields = ['book', 'borrower_name']
    
class BookOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOwned
        fields = ['book', 'bought_by']

class BookIsDonated(serializers.ModelSerializer):
    class Meta:
        model = BookOwned
        fields = ['book','is_donated','owned_id']

class BookLibrarySerializerDetails(serializers.ModelSerializer):
    # owner = BookIsDonated(many=True, source='owners')
    donated_count = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    # available = serializers.SerializerMethodField()


    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'release_date',
                  'description', 'price', 'publisher', 'isbn', 'genre', 
                  'cover', 'donated_count']

    def get_donated_count(self, obj):
        return obj.bookowned_set.filter(is_donated=True).count()
    
    def get_genre(self,obj):
        return json.loads(obj.genre)


class BookListLibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'cover']



class BookListLibraryBorrowSerializer(serializers.ModelSerializer):
    book_detail = serializers.SerializerMethodField()
    borrow_id = serializers.SerializerMethodField()

    class Meta:
        model = BookOwned
        fields = ['borrow_id','book_id','book_detail']

    def get_borrow_id(self, obj):
        return obj.owned_id

    def get_book_detail(self,obj):
        get_book = obj.book
        title = get_book.title
        author = get_book.author
        publisher = get_book.publisher
        cover = get_book.cover
        return {'title':title, 'author':author, 'publisher':publisher, 'cover':f'/media/{str(cover)}'}

class BookListLibraryOwnedSerializer(serializers.ModelSerializer):
    book_detail = serializers.SerializerMethodField()

    class Meta:
        model = BookOwned
        fields = ['owned_id','book_id','book_detail']

    def get_book_detail(self,obj):
        get_book = obj.book
        title = get_book.title
        author = get_book.author
        publisher = get_book.publisher
        cover = get_book.cover
        return {'title':title, 'author':author, 'publisher':publisher, 'cover':f'/media/{str(cover)}'}

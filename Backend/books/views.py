from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *

import datetime
import json


# Books Create
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('title', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('author', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('release_date', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('price', openapi.IN_FORM, type=openapi.TYPE_NUMBER),
        openapi.Parameter('publisher', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter(
                'genre',
                openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING),
                description="List of genres for the book"
            ),
    ],
    responses={
        status.HTTP_201_CREATED: openapi.Response(description='Book created successfully'),
        status.HTTP_400_BAD_REQUEST: openapi.Response(description='Bad request'),
    },
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_book(request):
    dict_book = request.data.dict()
    dict_book['genre'] = dict_book['genre'].split(',')
    publication_date = datetime.datetime.now().strftime('%Y-%m-%d')
    dict_book['publication_date'] = publication_date
    serializer = BookSerializer(data=dict_book)
    if serializer.is_valid():
        print(serializer.data)
        # serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Yang atas percobaan

# # Books Create
# @swagger_auto_schema(
#     method='post',
#     tags=['Books'],
#     manual_parameters=[
#         openapi.Parameter('title', openapi.IN_FORM, type=openapi.TYPE_STRING),
#         openapi.Parameter('author', openapi.IN_FORM, type=openapi.TYPE_STRING),
#         openapi.Parameter('release_date', openapi.IN_FORM, type=openapi.TYPE_STRING),
#         openapi.Parameter('price', openapi.IN_FORM, type=openapi.TYPE_NUMBER),
#         openapi.Parameter('publisher', openapi.IN_FORM, type=openapi.TYPE_STRING),
#         openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING),
#         openapi.Parameter(
#                 'genre',
#                 openapi.IN_FORM,
#                 type=openapi.TYPE_ARRAY,
#                 items=openapi.Items(type=openapi.TYPE_STRING),
#                 description="List of genres for the book"
#             ),
#     ],
#     responses={
#         status.HTTP_201_CREATED: openapi.Response(description='Book created successfully'),
#         status.HTTP_400_BAD_REQUEST: openapi.Response(description='Bad request'),
#     },
# )
# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def upload_book(request):
#     dict_book = request.data.dict()
#     publication_date = datetime.datetime.now().strftime('%Y-%m-%d')
#     dict_book['publication_date'] = publication_date
#     serializer = BookSerializer(data=dict_book)
#     if serializer.is_valid():
#         print(serializer.data)
#         # serializer.save() 
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Book Details with Title Name
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('title', openapi.IN_PATH, type=openapi.TYPE_STRING),
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(description='Details of the Book'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
    },
)
@api_view(['GET'])
def details_book(request,title):
    try:
        book = Book.objects.get(title__iexact=title)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response('Book Title not Found',status=status.HTTP_404_NOT_FOUND)

# List Books of Author
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('author', openapi.IN_PATH, type=openapi.TYPE_STRING),
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(description='Books by the Author'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
    },
)
@api_view(['GET'])
def books_by_author(request, author):
    books = Book.objects.filter(author__iexact=author)
    if not books.exists():
        return Response('No Books Found by this Author',status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# List Books of Publisher
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('publisher', openapi.IN_PATH, type=openapi.TYPE_STRING)
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(description='Books published by the Publisher'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
    },
)
@api_view(['GET'])
def books_by_publisher(request, publisher):
    books = Book.objects.filter(publisher__iexact=publisher)
    if not books.exists():
        return Response('No Books Found by this Publisher',status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# New Release Books
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    responses={
        status.HTTP_200_OK: openapi.Response(description='New Release Books'),
    }
)
@api_view(['GET'])
def new_release_books(request):
    books = Book.objects.order_by('-release_date')[:5]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# New Arival Books
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    responses={
        status.HTTP_200_OK: openapi.Response(description='New Arrival'),
    }
)
@api_view(['GET'])
def new_arival_books(request):
    books = Book.objects.order_by('-publication_date')[:5]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Donate Book
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('book_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
    ],
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def donate_book(request):
    if request.user.is_authenticated:
        book_id = request.data.get('book_id')
        try:
            book = Book.objects.get(id=book_id)
            books_donated = BookDonated.objects.filter(book_id=book_id)
            if not books_donated.exists():
                new_donation = BookDonated(book=book, number_of_donated=1)
                new_donation.save()
                return Response('Book Donated successfully', status=status.HTTP_201_CREATED)
            else:
                books_donated = books_donated.first()
                books_donated.number_of_donated += 1
                books_donated.save()
                return Response('Book Donated successfully', status=status.HTTP_201_CREATED)
        except Book.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)

# Borrow Book:
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('book_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
    ],
    responses={
        status.HTTP_201_CREATED: openapi.Response(description='Book borrowed successfully'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Book or Borrower not found'),
    },
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def borrow_book(request):
    if request.user.is_authenticated:
        book_id = request.data.get('book_id')
        borrower_name = request.user.username
        try:
            #Check if Book Exist in List of books and Check if person already borrowed or not
            book = Book.objects.get(id=book_id)

            #Check if User already Borrow or not
            try:
                borrower_check = BookBorrowed.objects.get(book_id=book_id, borrower_name=borrower_name, status_borrow='Borrowed')
                return Response('Book already borrowed by this borrower', status=status.HTTP_400_BAD_REQUEST)
                
            except BookBorrowed.DoesNotExist:

                #Check if Book is in library or not
                try:
                    get_from_library = BookDonated.objects.get(book_id=book_id)
                    
                    #Check if book quota is available or not
                    if get_from_library.number_of_donated > 0:
                        get_from_library.number_of_donated -= 1
                        new_borrow = BookBorrowed(book=book, borrower_name=borrower_name)
                        new_borrow.save()
                        get_from_library.save()
                        return Response('Book borrowed successfully', status=status.HTTP_201_CREATED)
                    else:
                        return Response('Book Quota not available', status=status.HTTP_400_BAD_REQUEST)

                except BookDonated.DoesNotExist:
                    return Response('Book not available in Library', status=status.HTTP_400_BAD_REQUEST)
        
        #If Book not Exist in List Books
        except Book.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)
    
# Returned Book
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('book_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
    ],
    responses={
        status.HTTP_201_CREATED: openapi.Response(description='Book returned successfully'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Book or Borrower not found'),
    },
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def returned_book(request):
    if request.user.is_authenticated:
        book_id = request.data.get('book_id')
        borrower_name = request.user.username
        try:
            book = Book.objects.get(id=book_id)

            try:
                borrower_check = BookBorrowed.objects.get(book_id=book_id, borrower_name=borrower_name, status_borrow='Borrowed')
                get_from_library = BookDonated.objects.get(book_id=book_id)
                borrower_check.status_borrow = 'Returned'
                get_from_library.number_of_donated += 1
                borrower_check.save()
                get_from_library.save()
                return Response('Book returned successfully', status=status.HTTP_200_OK)
            except BookBorrowed.DoesNotExist:
                return Response('Book not borrowed by this borrower', status=status.HTTP_404_NOT_FOUND)

        except Book.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)
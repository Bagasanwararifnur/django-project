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
        openapi.Parameter('isbn', openapi.IN_FORM, type=openapi.TYPE_STRING),
        openapi.Parameter('cover', openapi.IN_FORM, type=openapi.TYPE_FILE),
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
    dict_book['genre'] = json.dumps(dict_book['genre'].split(','))
    print(dict_book)
    publication_date = datetime.datetime.now().strftime('%Y-%m-%d')
    dict_book['publication_date'] = publication_date
    serializer = BookSerializer(data=dict_book)
    if serializer.is_valid():
        # print(serializer.data)
        serializer.save() 
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

#Book Bought
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('book', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ],
    responses={
        status.HTTP_201_CREATED: openapi.Response(description='Book borrowed successfully'),
        status.HTTP_400_BAD_REQUEST: openapi.Response(description='Bad request'),
    },
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def book_bought(request):
    if request.user.is_authenticated:
        data = request.data.dict()
        data['bought_by'] = request.user.username
        
        try:
            check_data = BookOwned.objects.get(bought_by=data['bought_by'],book_id=data['book'],is_donated=False)
            # print(check_data)
            return Response('You have already borrowed this book', status=status.HTTP_400_BAD_REQUEST)
        except BookOwned.DoesNotExist:
            serializers = BookOwnedSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('You must be logged in to borrow books', status=status.HTTP_401_UNAUTHORIZED)

# Donate Book
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('owned_id', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ],
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def donate_book(request):
    if request.user.is_authenticated:
        id = request.data.get('owned_id')
        username = request.user.username
        try:
            book = BookOwned.objects.get(owned_id=id)
            if book.bought_by == username:
                book.is_donated = True
                book.save()
                return Response('Book donated successfully', status=status.HTTP_200_OK)
            else:
                return Response('You are not the owner of this book', status=status.HTTP_403_FORBIDDEN)
        except BookOwned.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)

#Get Book
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(description='List of Books'),
    },
)
@api_view(['GET'])
@parser_classes([MultiPartParser,FormParser])
def get_books(request):
    book_id = request.GET.get('id')
    books = Book.objects.get(id=book_id)
    serializer = BookLibrarySerializerDetails(books)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
    books = Book.objects.filter(author__icontains=author)
    if not books.exists():
        return Response('No Books Found by this Author',status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List Book in Library
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    manual_parameters=[
        openapi.Parameter('pagination', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(description='List of Books in Library'),
    },
    operation_id="Get list of Books in Library per Page",
    operation_description="API ini digunakan untuk mendapatkan daftar buku yang tersedia di perpustakaan. "
                          "Anda dapat menggunakan parameter `pagination` untuk menentukan jumlah item per halaman.",
)
@api_view(['GET'])
def list_books(request):
    pagination = request.GET.get('pagination')
    if pagination == None:
        pagination = 0
    else:
        pagination = int(pagination)-1

    books = BookOwned.objects.filter(is_donated=True).values_list('book_id', flat=True).distinct()
    all_books = Book.objects.filter(id__in=books)[pagination*10:(pagination+1)*10]
    serializers = BookListLibrarySerializer(all_books, many=True)
    
    return Response(serializers.data,status=status.HTTP_200_OK)

# List Book in Borrowed Library
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    operation_id="Get list of Books in Borrowed Library",
    responses={
        status.HTTP_200_OK: openapi.Response(description='List of Books in Owner Library'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
    },
)
@api_view(['GET'])
def list_books_borrowed(request):
    if request.user.is_authenticated:
        books = BookOwned.objects.filter(borrower_name = request.user.username, is_borrowed=True)
        # books_list = Book.objects.filter(id__in=books)
        if not books.exists():
            return Response('No Books Found in Borrowed Library',status=status.HTTP_404_NOT_FOUND)
        serializer = BookListLibraryBorrowSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)
    
# List Book in Owned Library
@swagger_auto_schema(
    method='get',
    tags=['Books'],
    operation_id="Get list of Books in Owned Library",
    responses={
        status.HTTP_200_OK: openapi.Response(description='List of Books in Owner Library'),
        status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
    },
)
@api_view(['GET'])
def list_books_owned(request):
    if request.user.is_authenticated:
        books = BookOwned.objects.filter(bought_by = request.user.username, is_donated=False)
        if not books.exists():
            return Response('No Books Found in Owned Library',status=status.HTTP_404_NOT_FOUND)
        serializer = BookListLibraryOwnedSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)

# Returned Book
@swagger_auto_schema(
    method='post',
    tags=['Books'],
    operation_id="Return Book from Borrowed Library",
    manual_parameters=[
        openapi.Parameter('borrow_id', openapi.IN_FORM, type=openapi.TYPE_STRING),
    ],
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def returned_book(request):
    if request.user.is_authenticated:
        id = request.data.get('borrow_id')
        username = request.user.username
        
        try:
            book = BookOwned.objects.get(owned_id=id)
            if book.borrower_name == username:
                book.is_borrowed = False
                book.borrower_name = None
                book.save()
                return Response('Book returned successfully', status=status.HTTP_200_OK)
            else:
                return Response('You are not the borrower of this book', status=status.HTTP_403_FORBIDDEN)
        except BookOwned.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)


# # Book Details with Title Name
# @swagger_auto_schema(
#     method='get',
#     tags=['Books'],
#     manual_parameters=[
#         openapi.Parameter('title', openapi.IN_PATH, type=openapi.TYPE_STRING),
#     ],
#     responses={
#         status.HTTP_200_OK: openapi.Response(description='Details of the Book'),
#         status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
#     },
# )
# @api_view(['GET'])
# def details_book(request,title):
#     try:
#         book = Book.objects.get(title__iexact=title)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     except Book.DoesNotExist:
#         return Response('Book Title not Found',status=status.HTTP_404_NOT_FOUND)


# # List Books of Publisher
# @swagger_auto_schema(
#     method='get',
#     tags=['Books'],
#     manual_parameters=[
#         openapi.Parameter('publisher', openapi.IN_PATH, type=openapi.TYPE_STRING)
#     ],
#     responses={
#         status.HTTP_200_OK: openapi.Response(description='Books published by the Publisher'),
#         status.HTTP_404_NOT_FOUND: openapi.Response(description='Not Found'),
#     },
# )
# @api_view(['GET'])
# def books_by_publisher(request, publisher):
#     books = Book.objects.filter(publisher__iexact=publisher)
#     if not books.exists():
#         return Response('No Books Found by this Publisher',status=status.HTTP_404_NOT_FOUND)
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# # New Release Books
# @swagger_auto_schema(
#     method='get',
#     tags=['Books'],
#     responses={
#         status.HTTP_200_OK: openapi.Response(description='New Release Books'),
#     }
# )
# @api_view(['GET'])
# def new_release_books(request):
#     books = Book.objects.order_by('-release_date')[:5]
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# # New Arival Books
# @swagger_auto_schema(
#     method='get',
#     tags=['Books'],
#     responses={
#         status.HTTP_200_OK: openapi.Response(description='New Arrival'),
#     }
# )
# @api_view(['GET'])
# def new_arival_books(request):
#     books = Book.objects.order_by('-publication_date')[:5]
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# # # Donate Book
# # @swagger_auto_schema(
# #     method='post',
# #     tags=['Books'],
# #     manual_parameters=[
# #         openapi.Parameter('book_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
# #     ],
# # )
# # @api_view(['POST'])
# # @parser_classes([MultiPartParser, FormParser])
# # def donate_book(request):
# #     if request.user.is_authenticated:
# #         book_id = request.data.get('book_id')
# #         try:
# #             book = Book.objects.get(id=book_id)
# #             books_donated = BookDonated.objects.filter(book_id=book_id)
# #             if not books_donated.exists():
# #                 new_donation = BookDonated(book=book, number_of_donated=1)
# #                 new_donation.save()
# #                 return Response('Book Donated successfully', status=status.HTTP_201_CREATED)
# #             else:
# #                 books_donated = books_donated.first()
# #                 books_donated.number_of_donated += 1
# #                 books_donated.save()
# #                 return Response('Book Donated successfully', status=status.HTTP_201_CREATED)
# #         except Book.DoesNotExist:
# #             return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
# #     else:
# #         return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)

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
                borrower_check = BookOwned.objects.get(borrower_name=borrower_name, is_borrowed=True, book_id=book_id)
                return Response('Book already borrowed by this borrower', status=status.HTTP_400_BAD_REQUEST)
                
            except BookOwned.DoesNotExist:

                borrower_check = BookOwned.objects.filter(book_id=book_id,is_donated=True,is_borrowed=False).first()
                if borrower_check:
                    borrower_check.is_borrowed = True
                    borrower_check.borrower_name = borrower_name
                    borrower_check.save()

                    return Response('Book borrowed successfully', status=status.HTTP_201_CREATED)

                else:
                    return Response('No available copies of this book', status=status.HTTP_404_NOT_FOUND)
        
        #If Book not Exist in List Books
        except Book.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)
    
# # Returned Book
# @swagger_auto_schema(
#     method='post',
#     tags=['Books'],
#     manual_parameters=[
#         openapi.Parameter('book_id', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
#     ],
#     responses={
#         status.HTTP_201_CREATED: openapi.Response(description='Book returned successfully'),
#         status.HTTP_404_NOT_FOUND: openapi.Response(description='Book or Borrower not found'),
#     },
# )
# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def returned_book(request):
#     if request.user.is_authenticated:
#         book_id = request.data.get('book_id')
#         borrower_name = request.user.username
#         try:
#             book = Book.objects.get(id=book_id)

#             try:
#                 borrower_check = BookBorrowed.objects.get(book_id=book_id, borrower_name=borrower_name, status_borrow='Borrowed')
#                 get_from_library = BookDonated.objects.get(book_id=book_id)
#                 borrower_check.status_borrow = 'Returned'
#                 get_from_library.number_of_donated += 1
#                 borrower_check.save()
#                 get_from_library.save()
#                 return Response('Book returned successfully', status=status.HTTP_200_OK)
#             except BookBorrowed.DoesNotExist:
#                 return Response('Book not borrowed by this borrower', status=status.HTTP_404_NOT_FOUND)

#         except Book.DoesNotExist:
#             return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
#     else:
#         return Response('Authentication required', status=status.HTTP_401_UNAUTHORIZED)
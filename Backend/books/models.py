from django.db import models
from enum import Enum
import datetime
import uuid
import os

class StatusBorrow(Enum):
    Borrowed = 'Borrowed'
    Returned = 'Returned'

# Create your models here.

def renameBook(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{extension}'
    return os.path.join(f'cover/{new_filename}')


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    release_date = models.DateField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    genre = models.JSONField(default=list)
    cover = models.ImageField(upload_to=renameBook)

    def __str__(self):
        return self.title

class BookDonated(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number_of_donated = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Book: {self.book.title} - Donated: {self.number_of_donated}"

class BookBorrowed(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrow_date = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"),)
    due_date = models.DateField(default=(datetime.datetime.now()+datetime.timedelta(days=14)).strftime("%Y-%m-%d"))
    status_borrow = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in StatusBorrow], default=StatusBorrow.Borrowed.value)

    def __str__(self):
        return f"Book: {self.book.title}"

class BookOwned(models.Model):
    owned_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bought_by = models.CharField(max_length=100)
    is_donated = models.BooleanField(default=False)
    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Book: {self.book.title} - Bought by: {self.bought_by}"

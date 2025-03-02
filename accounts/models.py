from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True)
    bio = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)
    

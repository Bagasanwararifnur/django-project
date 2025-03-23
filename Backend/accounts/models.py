from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
import uuid


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True)
    bio = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)

class ForgotPassword(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expiry_date = models.DateTimeField()
    is_valid = models.BooleanField(default=True, null=False)

    def save(self, *args, **kwargs):
        self.expiry_date = timezone.now() + timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user.username}"
    

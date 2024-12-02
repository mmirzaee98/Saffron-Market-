from django.contrib.auth.models import AbstractUser
from django.db import models

# Model for handling profile data with abstract user
class Profile(AbstractUser):
    phone = models.CharField(max_length=13)
    address = models.TextField()
    national_id = models.CharField(max_length=10)

    def __str__(self):
        return self.username
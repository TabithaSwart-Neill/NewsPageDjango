from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # This is where to add a custom field
    pass

    def __str__(self):
        return self.username

# Create your models here.

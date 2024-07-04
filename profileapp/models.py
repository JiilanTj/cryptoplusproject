from django.db import models
from registrationapp.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Added default=1
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    walletaddress = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
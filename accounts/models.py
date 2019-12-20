from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, default="Данные не предоставлены еще")
    location = models.CharField(max_length=30, blank=True, default="Данные не предоставлены еще")
    birth_date = models.DateField(null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    image = models.ImageField(upload_to='profile_pic/', default='user.png', blank=True)
    cv = models.FileField(upload_to='cv/', null=True, verbose_name="cv", blank=True)

# Create your models here.

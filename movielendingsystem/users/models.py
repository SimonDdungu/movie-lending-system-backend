from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15, unique=True)
    NIN = models.CharField(max_length=20, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



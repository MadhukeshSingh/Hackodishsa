from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)
    subject = models.TextField(max_length=150)
    
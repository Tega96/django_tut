from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True) #Id is automatic in django, but we can still define it thus.
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_used = models.DateTimeField(auto=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("electronics", "Electronics"),
        ("books", "Books"),
        ("games", "Games"),
        ("cars", "Cars"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="products/")
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

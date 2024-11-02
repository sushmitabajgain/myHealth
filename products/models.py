from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    description = models.TextField()          # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created

    def __str__(self):
        return self.name  # String representation of the product

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)  # Product name
    overview = models.TextField()  # Short description or summary
    long_description = models.TextField()  # Detailed description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    poster = models.URLField(blank=True, null=True)  # URL to poster image
    image_local = models.ImageField(upload_to="products/", blank=True, null=True)  # Upload local image
    rating = models.FloatField(default=0.0)  # Rating out of 5 or 10
    in_stock = models.BooleanField(default=True)  # Availability
    size = models.CharField(max_length=50, blank=True, null=True)  # Size information
    best_seller = models.BooleanField(default=False)  # Bestseller status
    class Meta:
        db_table = 'bookstorebackend_products'  # Explicit table name


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    price = models.PositiveIntegerField( default=0)
    description = models.TextField(blank=True, null=True)
    data_create = models.DateTimeField(auto_now_add=True)
    sku = models.CharField( max_length=30, blank=True, null=True)

class ProductImage(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")   

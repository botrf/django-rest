from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    price = models.PositiveIntegerField( default=0)
    description = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)

class ProductImage(models.Model):
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")   
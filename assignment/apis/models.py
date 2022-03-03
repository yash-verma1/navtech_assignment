from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "Users"

class Products(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    class Meta:
        db_table = "Products"


class Orders(models.Model):
    user = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        db_table = "Orders"


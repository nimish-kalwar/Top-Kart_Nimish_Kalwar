from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class deal(models.Model):
    Product_id = models.CharField(max_length=150,null=True, blank=True)
    Product_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(default=timezone.now)
    Actual_price=models.FloatField(default=0)
    Final_price=models.FloatField(default=0)
    Total_units = models.PositiveIntegerField(default=0)
    Available_units = models.PositiveIntegerField(default=0)
    expired = models.BooleanField(default=False)

class Orders(models.Model):
    order_id= models.CharField(max_length=150,null=True, blank=True)
    Product_id = models.CharField(max_length=150,null=True, blank=True)
    Product_name = models.CharField(max_length=250)
    Ordered_at = models.DateTimeField(default=timezone.now)
    buyer_name = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    Ordered_price=models.FloatField(default=0)
    status = models.CharField(max_length=50, default="Received")
    
from django.db import models
from django.contrib import admin

class Amazon(models.Model):
    Phone_No=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    DoB=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Quantity=models.FloatField()

class AmazonAdmin(admin.ModelAdmin):
    list_display=["Phone_No","Name","DoB","Email","Address","Quantity"]
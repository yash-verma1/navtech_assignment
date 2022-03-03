from django.contrib import admin
from apis.models import Products

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryname']


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['categoryname', 'product_name', 'price', 'quantity', 'description']
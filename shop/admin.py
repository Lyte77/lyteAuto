from django.contrib import admin
from .models import Category, Car, Manufacturer

# Register your models here.

@admin.register(Category)
class CartegoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = { 'slug'}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'created',]

@admin.register(Manufacturer)
class CarAdmin(admin.ModelAdmin):
    list_display = ['country',]
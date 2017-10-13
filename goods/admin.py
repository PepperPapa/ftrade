from django.contrib import admin

# Register your models here.
from .models import Category, Goods

admin.site.register(Category)
admin.site.register(Goods)
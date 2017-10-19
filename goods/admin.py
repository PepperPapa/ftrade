from django.contrib import admin

# Register your models here.
from .models import Category, Goods

class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name", "recommended", "description", "category", "thumbnail1", "pub_date"]

admin.site.register(Category)
admin.site.register(Goods, GoodsAdmin)
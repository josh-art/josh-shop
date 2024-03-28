from django.contrib import admin
from django.contrib import admin
from .models import Category, Contacts, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Contacts)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']


    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)
# Register your models here.

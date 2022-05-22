from django.contrib import admin
from django.contrib import admin
from .models import Category, Contacts, Product,  Variation, ProductFeatured,Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Variation)
admin.site.register(ProductFeatured)
admin.site.register(Review)
admin.site.register(Contacts)

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        VariationInline,
    ]

    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)
# Register your models here.

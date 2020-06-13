from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title']
    list_display = ['title', 'description', 'price', 'active', 'updated']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
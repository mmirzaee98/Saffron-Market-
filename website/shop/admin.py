from django.contrib import admin
from shop.models import Product, ProductComment, Category, Invoice


# register shop models in admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','off_percentage','category','creator','owner','date_create','date_update']
    list_filter = ['price','off_percentage','category','creator','date_create','date_update']
    search_fields = ['name','owner']

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['user','text','rate','product','date']
    list_filter = ['user','rate','product','date']
    search_fields = ['user','text']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['user','total_price','tax','status','date_create','send_date']
    list_filter = ['user','total_price','status','date_create','send_date']
    search_fields = ['user','pk']

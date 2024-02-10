from django.contrib import admin
from django.utils.html import format_html
from . models import Doctor, Product, Category, Order
# Register your models here.

# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display=('dname','ddegree')

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def prdImg(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    
    list_display=('name','description', 'price', 'prdImg', 'cat')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('user', 'address', 'product', 'quantity', 'payment_status')


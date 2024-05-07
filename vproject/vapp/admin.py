from django.contrib import admin
from .models import Customer
from .models import Products

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display="vendor_id","name","contact_details","address","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate"
    
admin.site.register(Customer,CustomerAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display="name","price","description","image"
    
admin.site.register(Products)
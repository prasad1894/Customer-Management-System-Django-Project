from django.db import models

# Create your models here.

class Customer(models.Model):
    vendor_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def str(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
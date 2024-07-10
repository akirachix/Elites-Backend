from django.db import models

from django.utils import timezone
# from farmer_details.models import Farmers_details

# Create your models here.
class Products(models.Model):
    # farmers_id=models.ForeignKey('farmer_details.Farmers_details',on_delete=models.CASCADE,default=1)
    product_name =models.CharField(max_length=50)
    price =models.PositiveIntegerField()
    picture =models.ImageField()


    def __str__(self):
        return f'{self.product_name}'



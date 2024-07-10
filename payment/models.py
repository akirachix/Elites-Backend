from django.db import models
from django.utils import timezone
# from farmer_details.models import Farmers_details

# Create your models here.
class Payments(models.Model):
  # farmers_id=models.ForeignKey('farmer_details.Farmers_details',on_delete=models.CASCADE,default=1)
  inputs =models.PositiveIntegerField()
  amount_paid =models.DecimalField(max_digits=10,decimal_places=2)
  amount_deducted =models.DecimalField(max_digits=6,decimal_places=2)
  balance =models.PositiveIntegerField()



  def __str__(self):
        return f'{self.inputs}'


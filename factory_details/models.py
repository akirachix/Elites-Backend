from django.db import models

from farmers_details.models import Farmers_details

class Factory_details(models.Model):
    farmers_id = models.ForeignKey('farmers_details.Farmers_details', on_delete=models.CASCADE, default=1)
    factory_name = models.CharField(max_length=20)
    factory_email = models.EmailField()
    factory_location = models.CharField(max_length=20)
    factory_reg_no = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.factory_name}'
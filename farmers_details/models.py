from django.db import models

class Farmers_details(models.Model):
    farmers_id =models.IntegerField(default=1)
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    id_number =models.CharField(max_length=15)
    phone_number=models.PositiveSmallIntegerField()
   

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

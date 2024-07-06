from django.db import models

# Create your models here.
class Farmer_details(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    age=models.SmallIntegerField()
    gender =models.CharField(max_length=50)
    id_number =models.CharField(max_length=15)
    phone_number=models.PositiveSmallIntegerField()
    payment_due =models.PositiveBigIntegerField()
    input =models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
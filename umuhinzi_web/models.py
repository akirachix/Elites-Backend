from django.db import models

# Create your models here.
class Factory_details(models.Model):
    factory_name =models.CharField(max_length=20)
    factory_email =models.EmailField()
    factory_location =models.CharField(max_length=20)
    

   

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
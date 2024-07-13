from django.db import models
from django.utils import timezone  
from farmers_details.models import Farmers_details


class News(models.Model):
    farmers_id = models.ForeignKey('farmers_details.Farmers_details', on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    publishing_date = models.DateField(default=timezone.now)  
    author_name = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} by {self.author_name}'




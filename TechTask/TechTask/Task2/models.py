from pyexpat import model
from django.db import models

# Create your models here.
class EventDet(models.Model):
    name=models.CharField('Event Name',max_length=120)
    date=models.DateField('Date') 
    complete=models.BooleanField('Complete')
    description=models.TextField('Des')

    def __str__(self) -> str:
        return self.name
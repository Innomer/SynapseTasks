from pyexpat import model
from django.db import models

# Create your models here.
class EventDet(models.Model):
    name=models.CharField('Event Name',max_length=120)
    date=models.DateField('Date',null=True,blank=True) 
    complete=models.BooleanField('Complete',null=True,blank=True)
    description=models.TextField('Des')

    def __str__(self) -> str:
        return self.name
from django.db import models
#create your models
from django.db import models
class student(models.Model):
    stdno=models.IntegerField()
    stdname=models.CharField(max_length=50)
    stdmarks=models.FloatField()
    stdresult=models.CharField(max_length=255)

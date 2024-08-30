from django.db import models

# Create your models here.
class Faculty(models.Model):
    Fname=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    

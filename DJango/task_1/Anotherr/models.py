from django.db import models

# Create your models here.
class Anotherr(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    

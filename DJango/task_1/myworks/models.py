from django.db import models

class myworks(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image= models.ImageField()
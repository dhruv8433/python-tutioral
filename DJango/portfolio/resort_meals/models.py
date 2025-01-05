from django.db import models
from resort.models import resort

# Create your models here.
class resort_meals(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='resort_meals')
    refrence_resort = models.ForeignKey(resort, on_delete=models.CASCADE, default=1)
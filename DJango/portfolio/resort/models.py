from django.db import models

# Create your models here.
class resort(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='resort/')
    price = models.IntegerField()
    discount_price = models.IntegerField()
    offer = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.IntegerField()
    room = models.IntegerField()
    bed = models.IntegerField()


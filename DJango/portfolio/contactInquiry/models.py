from django.db import models

# Create your models here.
class contactInquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    message=models.TextField()
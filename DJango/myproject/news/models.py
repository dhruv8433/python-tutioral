from django.db import models

# Create your models here.
class news(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

class NewsAuthor(models.Model):
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    author_contact = models.IntegerField()
    author_address = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    name=models.ForeignKey("news", on_delete=models.CASCADE) 
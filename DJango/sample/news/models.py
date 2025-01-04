from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class news (models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()

    # slug field bnavi je automatic bnse tne admin ma entry nhi marvi pde
    news_slug=AutoSlugField(populate_from='title', unique=True,default=None,null=True)
    news_image = models.FileField(upload_to='news/', max_length=250, default=None, null=True)

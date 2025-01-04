from django.contrib import admin
from news.models import news

# Register your models here.
class newAdminModel(admin.ModelAdmin):
    list_display = ['title', 'content', 'news_image']

admin.site.register(news, newAdminModel)
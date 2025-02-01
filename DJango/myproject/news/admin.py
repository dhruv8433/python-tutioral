from django.contrib import admin
from .models import news,NewsAuthor
# Register your models here.
# @admin.register('news')
class newsAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ('title','description')
    list_filter = ('title','description')
    list_editable = ('description',)
    list_per_page = 10
    list_max_show_all = 120

admin.site.register(news,newsAdmin)    

class NewsAuthoradmin(admin.ModelAdmin):
    list_display = ('author_name','author_email','author_contact','author_address','published_date','name')

admin.site.register(NewsAuthor,NewsAuthoradmin)
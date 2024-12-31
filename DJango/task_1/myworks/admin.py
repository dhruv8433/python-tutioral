from django.contrib import admin
from myworks.models import myworks

class MyWorkModel(admin.ModelAdmin):
    list_display=("name","description","image")

admin.site.register(myworks, MyWorkModel)
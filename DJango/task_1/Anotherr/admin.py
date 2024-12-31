from django.contrib import admin
from Anotherr.models import Anotherr

#  Register your models here.
class AnotherrService(admin.ModelAdmin):
    list_display=("name","age","email")

admin.site.register(Anotherr,AnotherrService)    
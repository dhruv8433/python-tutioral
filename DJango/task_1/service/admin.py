from django.contrib import admin
from service.models import Service

class serviceAdmin(admin.ModelAdmin):
    list_display=("title","description")
# Register your models here.

# now register app in admin site

admin.site.register(Service,serviceAdmin)
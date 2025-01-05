from django.contrib import admin
from project.models import project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url')

admin.site.register(project, ProjectAdmin)
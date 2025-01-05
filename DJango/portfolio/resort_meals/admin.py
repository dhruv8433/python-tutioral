from django.contrib import admin
from resort_meals.models import resort_meals

# Register your models here.
class ResortMealsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'refrence_resort')

admin.site.register(resort_meals, ResortMealsAdmin)
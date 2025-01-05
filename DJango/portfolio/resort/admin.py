from django.contrib import admin
from resort.models import resort

# Register your models here.
class ResortAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'price', 'discount_price', 'offer', 'location', 'rating', 'review', 'room', 'bed')

admin.site.register(resort, ResortAdmin)
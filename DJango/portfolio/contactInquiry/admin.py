from django.contrib import admin

from contactInquiry.models import contactInquiry

class contactInquiryAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","message")

admin.site.register(contactInquiry,contactInquiryAdmin)
# Register your models here.

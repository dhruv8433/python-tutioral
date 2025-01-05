from django.contrib import admin
from django.urls import path
from portfolio import views
# setting import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('projects/', views.projectPage, name='projects'),
    path('contact/', views.contactPage, name='submit_inquiry'),
    path('thank-you/', views.thanksPage, name='thank-you'),
    path('about/', views.aboutPage, name='about'),
    path('resorts/', views.resortsPage, name='search_resorts'),
    path('resorts/<int:id>', views.resort_detail, name='resort_detail'),
    path('resorts/<int:id>/<str:category>', views.resortMeals, name='foods'),
]

# setting for media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
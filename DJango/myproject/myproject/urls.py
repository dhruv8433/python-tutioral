"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/",views.about_us,name="about"),
    path("submit_contact/",views.contact,name="contact form"),
    path("calc/",views.calc,name="calculator"),
    path("check-number/",views.check_number,name="check-number"),
    path("news/",views.news_show,name="news-show"),
    path("news/author/<str:name>",views.news_author,name="news-author"),
]
# int,slug,string
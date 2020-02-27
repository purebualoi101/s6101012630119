from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.calculator, name='home'),
    path('admin/', admin.site.urls),
    ]

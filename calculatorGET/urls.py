from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('calculator/', views.calculatorGET, name='home2'),
    path('admin/', admin.site.urls),
    ]

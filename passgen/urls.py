from django.urls import path
from . import views

urlpatterns = [

    path('', views.passgen, name='passgen'),
    path('passgen_output', views.passgen_output, name='passgen_output'),






]

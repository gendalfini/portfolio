from django.urls import path
from . import views

urlpatterns = [

    path('', views.caesar, name='caesar'),
    path('caesar_output', views.caesar_output, name='caesar_output'),






]

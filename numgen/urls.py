from django.urls import path
from . import views

urlpatterns = [

    path('', views.numgen, name='numgen'),
    path('numgen_output', views.numgen_output, name='numgen_output'),






]

from django.urls import path
from . import views

urlpatterns = [

    path('', views.downloader, name='downloader'),
    path('downloader_out', views.downloader_out, name='downloader_out'),






]

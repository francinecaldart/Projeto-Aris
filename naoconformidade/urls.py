from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
   path('', views.dashboard, name='Dashboard'),
   path('NC_create/', views.createNC, name='create_NC')


]
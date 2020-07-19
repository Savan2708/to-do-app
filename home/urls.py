from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('edit/<list_id>', views.edit, name="edit"),
]

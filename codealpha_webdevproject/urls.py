from django.urls import path
from django.contrib import admin
from todoApp import views

urlpatterns = [
    path('', views.index),  # Add this line to define the root URL
    path('todo/', views.todoApi),
    path('todo/<int:id>/', views.todoApi),
    path('admin/', admin.site.urls),
]


from django import forms
from .models import Task

from django.urls import path
from . import views

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


urlpatterns = [
    path('', views.index, name='index'),
    path('update-task/<str:pk>/', views.updateTask, name="update"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete")
]
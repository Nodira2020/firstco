from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("/index", index, name='index'),
    path("", update, name='update_task')
]

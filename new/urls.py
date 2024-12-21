from django.urls import path 
from.views import home_view, index_view

urlpatterns = [
    path("home/", home_view, name="home"),
    path("", index_view, name='index')
]

from django.urls import path
from .views import index, home

urlpatterns = [
    path("" ,index, name = "name" ),
    path("home/",home, name = "home" )
]

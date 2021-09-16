from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hellow world")

def home(request):
    return HttpResponse("I am in home")





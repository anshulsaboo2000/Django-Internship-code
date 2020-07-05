from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cse(request):
    return HttpResponse("Welcome to CSE Department")

def etc(request):
    return HttpResponse("Welcome to ETC Department")

def mech(request):
    return HttpResponse("Welcome to MECH Department")

def civil(request):
    return HttpResponse("Welcome to Civil Department")
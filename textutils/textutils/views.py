#I have created this file - Jay
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello Jay! It's Django Speaking")

def about(request):
    return HttpResponse("<h1>About Django</h1>")

def removepunc(request):
    return HttpResponse("REMOVE PUCHTUATION")

def capitalizefirst(request):
    return HttpResponse("CAPTALIZE FIRST")
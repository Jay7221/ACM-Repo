#file created by Jay

from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href = "H.COM"> Code With Harry</a>')

def home(request):
    return HttpResponse("Home")
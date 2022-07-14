from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    # return HttpResponse('<h1>Rhyl Home</h1>')  # simple response
    return render(request, 'r1pyle/home.html')      # render method

def about(request):
    # return HttpResponse('<h1>Rhyl About</h1>')  # simple response
    return render(request, 'r1pyle/about.html')      # render method

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Aug 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Aug 28 2018'
    }
]

def home(request):
    context ={
        'posts': posts
    }
    # return HttpResponse('<h1>Rhyl Home</h1>')  # simple response
    return render(request, 'rhyl/home.html', context)      # render method

def about(request):
    # return HttpResponse('<h1>Rhyl About</h1>')  # simple response
    return render(request, 'rhyl/about.html')      # render method

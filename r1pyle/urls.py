from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='r1pyle-home'),
    path('about/', views.about, name='r1pyle-about'),
]

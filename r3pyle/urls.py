from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='r3pyle-home'),
    path('about/', views.about, name='r3pyle-about'),
]

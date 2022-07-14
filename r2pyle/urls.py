from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='r2pyle-home'),
    path('about/', views.about, name='r2pyle-about'),
]

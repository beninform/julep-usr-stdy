from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bala-home'),
    path('about/', views.about, name='bala-about'),
]

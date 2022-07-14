from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rhyl-home'),
    path('about/', views.about, name='rhyl-about'),
]

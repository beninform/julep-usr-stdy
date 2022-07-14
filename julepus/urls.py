"""julepus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rhyl/', include('rhyl.urls')),  # make the rhyl home a non-default
    path('', include('rhyl.urls')),       # make the rhyl home the default
    path('bala/', include('bala.urls')),       # the bala home
    path('r1pyle/', include('r1pyle.urls')),       # the r1pyle home
    path('r2pyle/', include('r2pyle.urls')),       # the r2pyle home
    path('r3pyle/', include('r3pyle.urls')),       # the r3pyle home
]

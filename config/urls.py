"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render
from datetime import date


admin.site.site_header = 'Panel de control de WeDomotic'
admin.site.index_title = 'Administracion del sitio'
admin.site.site_title = 'Wedomotic'

def homepage(request):
	return render(request, 'homepage.html',{'year':date.today().year})

def about(request):
    return render(request, 'about.html')

def error404(request):
    return render(request, '404.html')

urlpatterns = [
    path('admin/', admin.site.urls, name = 'panel'),
    path('', homepage, name = 'homepage'),
    path('', include('products.urls')),
    path('clients/', include('clients.urls')),
    path('auth/', include('users.urls')),
    path('about/', about, name = 'about'),
    path('404/', error404, name = '404')
]

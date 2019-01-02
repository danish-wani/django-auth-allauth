"""authorization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django_auth.views import Signup, logout
urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django_auth.urls')),
    path('allauth/', include('django_allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # for django_auth
    path('signup/', Signup.as_view(), name='signup'),
    path('logout_login/', logout, name='logout_login'),

]
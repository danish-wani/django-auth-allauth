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
from django.urls import path, include, re_path
from django_allauth.views import Navigate


urlpatterns = [
    path('admin/', admin.site.urls),


    # path('', Navigate.as_view(), name='navigate'),
    # path('auth/', include('django_auth.urls', namespace='auth')),
    path('', include('django_allauth.urls', namespace='all_auth')),
    # path('auth_accounts/', include('django.contrib.auth.urls')), # for django_auth
    # path('signup/', Signup.as_view(), name='signup'), # for django_auth
    # path('logout_login/', logout, name='logout_login'), # for django_auth

    re_path('^accounts/', include('allauth.urls')),

]

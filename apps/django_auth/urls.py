from django.urls import re_path, path
from .views import Home, activate

app_name = 'django_auth'

urlpatterns = [

    path('',Home.as_view(), name='home'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),

]
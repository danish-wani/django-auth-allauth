from django.shortcuts import render
from django.views import View


class Navigate(View):

    def get(self, request, *args, **kargs):
        return render(request, 'navigator.html')


class Home(View):
    def get(self, request, *args, **kargs):
        return render(request, 'allauth.html')


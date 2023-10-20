from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'name':'Мария'
        }
    return render(request, 'hr_app/home.html', context=data)


def about_me(request, what):
    return render(request, 'hr_app/about.html', context={'slug':what})




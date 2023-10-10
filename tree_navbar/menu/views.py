from django.shortcuts import render


def index(request, name):
    return render(request, 'menu/home.html', {'name': name})

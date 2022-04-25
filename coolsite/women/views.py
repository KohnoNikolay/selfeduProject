from django.http import HttpResponse
from django.shortcuts import render


def index(request):  #HttpResponse
    return HttpResponse("Страница приложения women")


def categories(request):  #HttpResponse
    return HttpResponse("<h1>Статьи по категориям</h1>")


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hello!')
    return render(request, 'memories/index.html', {})


def detail(request):
    # return HttpResponse('Detail')
    return render(request, 'memories/detail.html', {})


def add(request):
    # return HttpResponse('add')
    return render(request, 'memories/add.html', {})

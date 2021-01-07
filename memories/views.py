from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'memories/login.html')


@login_required
def detail(request):
    return render(request, 'memories/detail.html')


def add(request):
    return render(request, 'memories/add.html', {})

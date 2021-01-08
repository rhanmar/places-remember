from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from memories.models import Point, Place


def login(request):
    """
    View to log in
    """
    return render(request, 'memories/login.html')


@login_required
def detail(request):
    """
    View to show information about User's memories
    """
    return render(request, 'memories/detail.html', {'places': request.user.place_set.all()})


def add(request):
    """
    View to Add memory
    """
    if request.method == 'POST':
        user = request.user
        point = Point.objects.create(latitude=request.POST['lat'], longitude=request.POST['long'])
        Place.objects.create(name=request.POST['name'], comment=request.POST['comment'], author=user, point=point)
        return redirect('detail')
    return render(request, 'memories/add.html')

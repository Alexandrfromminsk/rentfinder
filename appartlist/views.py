from django.shortcuts import render
from django.http import HttpResponse
from .models import Apt

def all_appartments_view(request):
    apts=Apt.objects.all()
    return render(request, 'apt_list.html', {"apts":apts})

def map_view(request):
    return render(request, 'map.html')

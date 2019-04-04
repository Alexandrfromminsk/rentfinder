from django.shortcuts import render
from django.http import HttpResponse

def all_appartments_view(request):
    return HttpResponse("All appartments list")

# Create your views here.

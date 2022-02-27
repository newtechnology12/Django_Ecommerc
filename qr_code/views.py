from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    name = 'welcome'
    obj = Website.objects.get(id=1)
    context = {
        'name': name,
        'obj': obj,
    }
    return render(request, 'qrcod/home.html', context)
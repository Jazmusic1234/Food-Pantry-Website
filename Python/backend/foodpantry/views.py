from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PantryItem

# Create your views here.

def mainpage(request):
    context = {
        "items": PantryItem.objects.all()
    }
    return render(request, 'foodpantry/mainpage.html', context)

def aboutpage(request):
    return render(request, 'foodpantry/about.html')


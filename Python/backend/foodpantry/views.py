from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pantryView(request):
    return HttpResponse('Welcome to the Food Pantry')
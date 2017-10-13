from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Product(request):
    return HttpResponse("Welcome Goods products page!")
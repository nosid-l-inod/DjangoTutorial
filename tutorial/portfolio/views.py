# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is a basic view
def index(request):
    return HttpResponse("This is the portfolio index page")
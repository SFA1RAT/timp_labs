from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django import template


def static_html(request):
    return render(request, 'templates/static_handler.html')


def home(request):
    return render(request, 'templates/index.html');

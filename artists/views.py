"""
Django Views Documentation

These views handle HTTP requests and render corresponding HTML templates.

Functions:
    home(request): Renders the 'index.html' template for the home page.
    catalogue(request): Renders the 'catalogue.html' template for the catalogue page.
"""

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def catalogue(request):
    return render(request, 'catalogue.html')

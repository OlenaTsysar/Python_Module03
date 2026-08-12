from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpRequest("Index")

def about(request):
    return HttpRequest('About')

def contact(request):
    return HttpRequest('Contact')

def product_list(request):
    return HttpRequest('Product_list')

def product_detail(request, pk):
    return HttpRequest('Product_detail')

def login_view(request):
    return HttpRequest('Login_view')

def register_view(request):
    return HttpRequest('Register_view')

def logout_view(request):
    return HttpRequest('Logout_view')

# Create your views here.

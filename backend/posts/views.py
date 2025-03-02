from django.shortcuts import render
from django.http import HttpResponse as response
# Create your views here.

def index(request):

    return response("<h1>Vamos testar essa bagaça</h1>")
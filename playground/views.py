from django.shortcuts import render
from django.http import HttpResponse

# Handler to print hello world
def say_hello(request):
    return HttpResponse('Hello world')
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world")

def register(request):
    return render(request,'userauth/register.html')

def confirmation(request):
    return HttpResponse("First: {} Last: {} Email: {}".format(request.POST['firstname'], request.POST['lastname'], request.POST['email']))


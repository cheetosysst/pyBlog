from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Yes, this is working")
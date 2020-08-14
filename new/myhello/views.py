from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("my page 응답!")
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django!")
def intro(request):
    return render(request,'hello/intro.html')
# Create your views here.

from django.http import JsonResponse
def simpleapi(request):
    name01 = request.GET['name']
    age02 = request.GET['age']
    requestDict = request.GET
    result = int(age02) + 5
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)
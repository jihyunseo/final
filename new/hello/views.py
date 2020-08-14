from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
def XORwithKeras(first, second):
    new_model = tf.keras.models.load_model('hello/XORwithKeras.h5')
    param = [int(first), int(second)]
    result = new_model.predict([param])
    return result
def home(request):
    data=request.GET.copy()
    #{'first':'Jenna','second':'seo'}
    return render(request,'hello/home.html',context=data)
def form(request):
    return render(request,'hello/form.html')
def template(request):
return render(request, 'hello/template.html')



# Create your views here.

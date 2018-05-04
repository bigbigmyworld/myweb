from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello, 颜淼淼是只驴.</h1>")
    return render(request, 'index1.html')
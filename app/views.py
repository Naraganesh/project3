from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def silk(request):
    return HttpResponse('we are not talking about dairy milk silk') 

def dhoni(request):
    return HttpResponse('dhoni is best captain')
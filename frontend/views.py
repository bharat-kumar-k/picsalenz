from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery
# Create your views here.
def index1 (request):




    return render(request,'index1.html')
    
 

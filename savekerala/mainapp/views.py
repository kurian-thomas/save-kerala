import time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from django.views import View

from .models import *

def home(request):
	data={}
	return render(request,'mainapp/index.html',data)

def helplinenumbers(request):
	data={}
	return render(request,'mainapp/no.html',data)

def disastercamps(request):
	data={}
	return render(request,'mainapp/disaster.html',data)
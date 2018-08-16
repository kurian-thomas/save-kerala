import time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from django.views import View

from .forms import *
from .models import *

def home(request):
	data={}
	return render(request,'mainapp/index.html',data)

def helplinenumbers(request):
	data={}
	all_helplinenumber=helplinenumber.objects.all()
	data[all_helplinenumber]=all_helplinenumber
	if request.method == 'POST':
		form = helplinenumberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/helplinenumbers')
		else:
			return redirect('home')
	else:
		form=helplinenumberForm()
		data['form']=form
		return render(request,'mainapp/no.html',data)

def disastercamps(request):
	data={}
	return render(request,'mainapp/disaster.html',data)
import time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from django.views import View

from .forms import *
from .models import *

def home(request):
	data={}
	all_news=news.objects.all()
	data['all_news']=all_news
	if request.method == 'POST':
		form=newsForm(request.POST,request.FILES)
		print(request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/home')
		else:
			return redirect('/helplinenumbers')
	else:
		form=newsForm()
		data['form']=form
		return render(request,'mainapp/index.html',data)

def helplinenumbers(request):
	data={}
	all_helplinenumber=helplinenumber.objects.all()
	data['all_helplinenumber']=all_helplinenumber
	if request.method == 'POST':
		form = helplinenumberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/helplinenumbers')
		else:
			return redirect('/home')
	else:
		form=helplinenumberForm()
		data['form']=form
		return render(request,'mainapp/no.html',data)

def disastercamps(request):
	data={}
	return render(request,'mainapp/disaster.html',data)

def floodmaps(request):
	data={}
	return render(request,'mainapp/floodmaps.html',data)
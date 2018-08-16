from django.db import models
from django import forms

class helplinenumber(models.Model):
	name=models.CharField(max_length=255,blank=True)
	phonenumber=models.BigIntegerField(blank=True)
	def __str__(self):
		return self.name
class news(models.Model):
	desc=models.CharField(max_length=25500,blank=True)
	def __str__(self):
		return self.desc
from .models import *

class helplinenumberForm(forms.ModelForm):
	class Meta:
		model=helplinenumber
		fields=('name','phonenumber')

class newsForm(forms.ModelForm):
	class Meta:
		model=news
		fields=('desc','photo')
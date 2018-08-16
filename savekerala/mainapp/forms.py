from .models import *

class helplinenumberForm(forms.ModelForm):
	class Meta:
		model=helplinenumber
		fields=('name','phonenumber')
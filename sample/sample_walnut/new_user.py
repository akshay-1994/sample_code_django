from django import forms
from django.forms import ModelForm
from sample_walnut.models import UserDetails

class NewUserCreation(ModelForm):
	class Meta(object):
		"""docstring for Meta"""
		model=UserDetails
		fields=('Username','Useremail','PatientID')


		
			
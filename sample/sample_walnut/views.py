# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.generic import View
from datetime import datetime,timedelta
from sample_walnut.models import UserDetails
from sample_walnut.new_user import NewUserCreation
from sample_walnut.Serializers import UserDetailsSerializer
# Create your views here.

def get_user_details():
		queryset=UserDetails.objects.all()
		serializer_class=UserDetailsSerializer


def new_user_(request):
	user=NewUserCreation(request.POST)
	if user.is_valid():
		user_created=form.save()
		return render_to_response(request,'templates/user.html',{'patientID':user_created.PatientID,
			'username':user_created.Username,'email':user_created.Useremail
			})
	else:
		HttpResponse('User Creation Failed!')
			

class UserDetailsViewSet(View):

	def post(self,request):
		new_user_(request)

	def get(self,request):
		get_user_details()


	
		
	
			
		
	

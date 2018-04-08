# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetails(models.Model):
	Username= models.CharField(max_length=255)
	Useremail=models.EmailField()
	PatientID=models.IntegerField(primary_key=True,default=0,editable=True,unique=True)
    
    #def __unicode__(self):
	#	return "{0} {1} {2} {3} {4} ".format(
    #		self,self.Username,self.Useremail,self.PatientID)
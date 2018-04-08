from sample_walnut.models import UserDetails
from rest_framework import serializers

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for UserDetailsSerializer"""
	class Meta:
		model=UserDetails
		fields=('Username','Useremail','PatientID')
		
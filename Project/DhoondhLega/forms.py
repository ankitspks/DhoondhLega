from django import forms
from .models import House
class HouseForm(forms.ModelForm):
 	class Meta:
 		model = House
 		fields = [
 			"customer",
 			"address",
 			"description",
 			"contact",
 			"house_type",
 			"price",
 			"photos"
 		]
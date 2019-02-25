
from django import forms

class PublicForm(forms.Form):
	CHOICES = (
		('100','100'),
		)
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	phone_number = forms.CharField(widget=forms.NumberInput(attrs={"class":'form-control'}))


from django import forms

class StudentForm(forms.Form):
	school_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	student_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	student_id_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	student_father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	student_mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

from django import forms

class PublicForm(forms.Form):
	CHOICES = (
		('100','100'),
		)
	name = forms.CharField(
						widget=forms.TextInput(
											attrs={
													'class':'form-control'
													}
												)
						)

	father_name = forms.CharField(
							widget=forms.TextInput(
													attrs={
															'class':'form-control'
															}
													)
							)

	mother_name = forms.CharField(
							widget=forms.TextInput(
													attrs={
															'class':'form-control'
															}
													)
							)

	email = forms.CharField(
							widget=forms.TextInput(
													attrs={
															'class':'form-control'
															}
													)
							)

	phone_number = forms.CharField(
								widget=forms.NumberInput(
														attrs={
																"class":'form-control'
																}
														)
								)
	

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get("phone_number")
		if len(phone_number) != 10:
			raise forms.ValidationError("Enter a valid phone Number")
		return phone_number

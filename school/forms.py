
from django import forms

class StudentForm(forms.Form):
	school_name = forms.CharField(
					widget=forms.TextInput(
								attrs={
									'class':'form-control
									}
								)
				)

	student_name = forms.CharField(
					widget=forms.TextInput(
								attrs={
									'class':'form-control'
									}
								)
					)

	student_father_name = forms.CharField(
					widget=forms.TextInput(
								attrs={
									'class':'form-control'
									}
								)
						)

	student_mother_name = forms.CharField(
					widget=forms.TextInput(
								attrs={
									'class':'form-control'
									}
								)
				)

	student_age = forms.CharField(
				widget=forms.NumberInput(
							attrs={
								'class':'form-control'
								}
							)
				)

	student_class = forms.CharField(
				widget=forms.NumberInput(
							attrs={
								'class':'form-control'
								}
							)
					)

	def clean_student_age(self):
		student_age = self.cleaned_data.get("student_age")
		if student_age < str(12) or student_age > str(18):
			raise forms.ValidationError("Your age!! you should be > 12 and < 18")
		return student_age

	def clean_student_class(self):
		student_class = self.cleaned_data.get("student_class")
		if student_class > str(12):
			raise forms.ValidationError("I think 12th is the highes class?")
		return student_class

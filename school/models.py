
from django.db import models

class OwnerSchool(models.Model):
	name 		=		 models.CharField(max_length=100)
	title 		=		 models.CharField(max_length=200)
	message 	=		 models.TextField()
	date 		=		 models.DateField(null=True)
	time_left 	=		 models.DateField(null=True)

	def __str__(self):
		return self.name

class StudentRegistration(models.Model):
	student_school 			=		 	models.CharField(max_length=100)
	student_name 			=		 	models.CharField(max_length=100)
	student_father_name 		=			models.CharField(max_length=100)
	student_mother_name 		=		 	models.CharField(max_length=100)
	student_age 			=		 	models.IntegerField()
	student_class 			=		 	models.IntegerField()

	def __str__(self):
		return self.student_name

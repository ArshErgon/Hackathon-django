
from django.db import models

class OwnerSchool(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField(null=True)
	time_left = models.DateField(null=True)
	message = models.TextField()

	def __str__(self):
		return self.name


class RegisterSchool(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	school_image = models.ImageField(upload_to="SchImg")

	def __str__(self):
		return self.name

class StudentRegistration(models.Model):
	student_school = models.ForeignKey(RegisterSchool, on_delete=models.CASCADE)
	student_name = models.CharField(max_length=100)
	student_id = models.IntegerField()
	student_father_name = models.CharField(max_length=100)
	student_mother_name = models.CharField(max_length=100)

	def __str__(self):
		return self.student_name


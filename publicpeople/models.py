from django.db import models

class PublicRegistration(models.Model):
	person_name = models.CharField(max_length=100)
	person_father_name = models.CharField(max_length=100)
	person_mother_name = models.CharField(max_length=100)
	person_email = models.EmailField()
	person_phone_number = models.IntegerField()
	person_message = models.TextField()

	def __str__(self):
		return person_name
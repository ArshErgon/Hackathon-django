
from django.shortcuts import render

from .models import OwnerSchool

from .forms import StudentForm

def home(request):
	school_banner = OwnerSchool.objects.all()
	for x in school_banner:
		pass
	time_left = x.time_left
	print(time_left== True)
	return render(request, 'home.html', {'school_banner':school_banner, 'time_left':time_left})


def signin_page(request):
	form = StudentForm()
	return render(request, 'form/sign-student.html', {'form':form})

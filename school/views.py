
from django.shortcuts import render, redirect

from .models import OwnerSchool, StudentRegistration

from .forms import StudentForm

from publicpeople.models import PublicRegistration

def home(request):
	school_banner = OwnerSchool.objects.all()
	for x in school_banner:
		pass
	time_left = x.time_left
	a = PublicRegistration.objects.all()
	b = StudentRegistration.objects.all()
	total = len(a) + len(b)
	return render(request, 'home.html', {'school_banner':school_banner, 'time_left':time_left, 'total':total})


def signin_page(request):
	form = StudentForm(request.POST or None)
	if request.method == "POST":
		school_name = request.POST.get("school_name")
		student_name = request.POST.get("student_name")
		student_father_name = request.POST.get("student_father_name")
		student_mother_name = request.POST.get("student_mother_name")
		student_age = request.POST.get("student_age")
		student_class = request.POST.get("student_class")
		StudentRegistration.objects.create(
						   student_school		=		school_name, 
						   student_name			=		student_name, 
						   student_father_name 		=		student_father_name, 
						   student_mother_name 		=		student_mother_name, 
						   student_age			=		student_age, 
						   student_class		=		student_class)
		return redirect("/thank/you/")
	return render(request, 'form/sign-student.html', {'form':form})


def thank_page(request):
	return render(request, 'form/thank.html')

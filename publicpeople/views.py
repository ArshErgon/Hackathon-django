
from django.shortcuts import render, redirect

from .forms import PublicForm

from .models import PublicRegistration

def public_sign_page(request):
	form = PublicForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			if request.POST.get("radio") == "on":
				name = request.POST.get('name')
				father_name = request.POST.get('father_name')
				mother_name = request.POST.get("mother_name")
				email = request.POST.get("email")
				phone_number = request.POST.get("phone_number")
				PublicRegistration.objects.create(person_name 				=		name, 
												  person_father_name 		=		father_name, 
												  person_mother_name 		=		mother_name, 
												  person_email 				=		email, 
												  person_phone_number 		=		phone_number
												  )
				return redirect("/thank/you/")

	return render(request, 'form/sign-public.html',{'form':form})
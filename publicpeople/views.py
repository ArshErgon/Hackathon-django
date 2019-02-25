from django.shortcuts import render

from .forms import PublicForm


def public_sign_page(request):
	form = PublicForm()
	return render(request, 'form/sign-public.html',{'form':form})
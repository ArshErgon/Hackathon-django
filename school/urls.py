

from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name='home'),
	path("sign/", views.signin_page, name='signin'),
]

from .models import OwnerSchool

print("Urls patterns  herer -----")
print(OwnerSchool.objects.all())



from django.urls import path

from . import views
from publicpeople.views import public_sign_page

urlpatterns = [
	path("", views.home, name='home'),
	path("student/sign/", views.signin_page, name='student-sign'),
	path('public/sign/', public_sign_page, name='public-sign')
]

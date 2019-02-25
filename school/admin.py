from django.contrib import admin

from .models import OwnerSchool, StudentRegistration

admin.site.register(OwnerSchool)
admin.site.register(StudentRegistration)
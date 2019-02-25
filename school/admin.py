from django.contrib import admin

from .models import OwnerSchool, RegisterSchool, StudentRegistration

admin.site.register(OwnerSchool)
admin.site.register(RegisterSchool)
admin.site.register(StudentRegistration)
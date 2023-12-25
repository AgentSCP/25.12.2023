from django.contrib import admin
from .models import Student, Course, Person, Account, Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Account)
admin.site.register(Enrollment)

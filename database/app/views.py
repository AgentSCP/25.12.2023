from django.shortcuts import render
from .models import Student, Course, Account, Person

def index(request):
    python = Course.objects.get(name='Python')
    # student = python.student_set.get_or_create(name='Bob')
    student = Student.objects.create(name='Tom')
    python.student_set.add(student)
    st = Student.objects.get(id=3)
    his = Course.objects.gwt(id="History")
    his.student_set.add(st)
    res = Student.objects.get(id=3).course.all()

    sam = Person.objects.create(name='ogenmo')
    # res, _ = Account.objects.get_or_create(login='Sam123', password='12345678', user=sam)
    # res = Account.objects.get(user__id=3)
    # res.user.name = 'Samuel'
    # res.save()
    # acc = Account(login='gormtnj', password='foernfg')
    # sam.account = acc
    # sam.account.save()
    sam = Person.objects.get(account__login='fongofj')
    return render(request, 'app/index.html', context={'students': res})
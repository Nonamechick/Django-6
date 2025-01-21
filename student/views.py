from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='Wa') | Student.objects.filter(surname__startswith='Won')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='Wa') | ~Q (surname__startswith='Won') | Q (surname__startswith='Jane'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

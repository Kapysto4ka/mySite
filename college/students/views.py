from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def other(request,name):
    first_name, last_name = name.split('_')
    student = Student.objects.filter(name=first_name, surname=last_name).first()
    if student is not None:
        print(student.name)
        return render(request, 'students/index7.html', {'student': student})
    else:
        return HttpResponse(f"Student with name '{name}' not found")
def index(request):
    students = Student.objects.all()
    return render(request, 'students/index6.html', {'students': students})
def bilogan(request):
    return render(request, 'students/index.html')

def hrubuk(request):
    return render(request, 'students/index2.html')

def babyak(request):
    return render(request, 'students/index3.html')

def ivanyuk(request):
    return render(request, 'students/index4.html')

def all_students(request):
    return render(request, 'students/index5.html')
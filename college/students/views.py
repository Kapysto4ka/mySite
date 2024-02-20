from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

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
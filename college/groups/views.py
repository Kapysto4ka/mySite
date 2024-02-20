from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'groups/index.html')
def KI(request):
    name = 'KI-20-01'
    amount = '27'
    curator = 'Ольга Білан'
    return render(request,'groups/index2.html', {"name":name, "amount":amount, "curator": curator})

def AK(request):
    name = 'AK-20-01'
    amount = '25'
    curator = 'Василь Грималюк'
    return render(request,'groups/index2.html', {"name":name, "amount":amount, "curator": curator})

def PI(request):
    name = 'PI-21-02'
    amount = '29'
    curator = 'Ольга Стражник'
    return render(request,'groups/index2.html', {"name":name, "amount":amount, "curator": curator})

def FB(request):
    name = 'FB-23-01'
    amount = '15'
    curator = 'Ірина Вовк'
    return render(request,'groups/index2.html', {"name":name, "amount":amount, "curator": curator})
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Group


def groups(request,name):
    group = Group.objects.filter(name=name).first()
    if group is not None:
        info = {'group': group}
        return render(request, 'groups/index2.html', info)
    else:
        return HttpResponse(f"Group with name '{name}' not found")
def index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups': groups})

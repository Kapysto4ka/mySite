from django.shortcuts import render
from django.http import HttpResponse
import groups.models
import students.models
from django.core.files.base import ContentFile
import base64

def index(request):
    return render(request, 'manager/index.html')


def manager(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "student":
            name = request.POST.get("nameInput")
            surname = request.POST.get("secondInput")
            group = request.POST.get("input_3")
            age = request.POST.get("input_4")
            score = request.POST.get("input_5")
            image_data = request.FILES.get("fileToUpload")
            print(image_data)
            if image_data:
                student = students.models.Student.objects.create(name=name, surname=surname, group=group, age=age,
                                                             score=score, image=image_data)
                return HttpResponse(f"Student added: {name} {surname}")
        elif action == "group":
            name = request.POST.get("nameInput")
            curator = request.POST.get("secondInput")
            amount = int(request.POST.get("input_3"))
            average_score = request.POST.get("input_4")
            rating = int(request.POST.get("input_5"))
            group = groups.models.Group.objects.create(name=name, amount=amount, curator=curator,
                                                       average_score=average_score, rating=rating)
            return HttpResponse(f"Group added: {name}")
    return HttpResponse("Invalid request")

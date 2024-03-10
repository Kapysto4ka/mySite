from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_students, name="main"),
    path("other", views.index),
    path("other/<str:name>", views.other),
    path("bilogan", views.bilogan, name="index"),
    path("hrubuk", views.hrubuk, name="index"),
    path("babyak", views.babyak, name="index"),
    path("ivanyuk", views.ivanyuk, name="index"),
]
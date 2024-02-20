from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("KI-20-01", views.KI),
    path("AK-20-01", views.AK),
    path("PI-21-02", views.PI),
    path("FB-23-01", views.FB),
]
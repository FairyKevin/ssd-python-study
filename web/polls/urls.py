from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("info/", views.info),
    path("info/detail/<str:id>", views.detail),
]
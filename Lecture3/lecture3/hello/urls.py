from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sara", views.sara, name = "sara"),
    path("<str:name>", views.greet, name = "greet")
]
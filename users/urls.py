from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("list/", views.person_list, name="list"),
]

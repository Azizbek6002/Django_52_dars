from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path('', lambda request: redirect('register/')),
]

from django.shortcuts import render, redirect
from .models import Person

def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")

        Person.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            company=company
        )
        return redirect("list")

    return render(request, "register.html")


def person_list(request):
    people = Person.objects.all().order_by("-created_at")
    return render(request, "list.html", {"people": people})

from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "company", "created_at")
    search_fields = ("full_name", "email", "phone")

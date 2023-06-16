from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("text", "file", "date_created")
    empty_value_display = "--empty--"
    list_filter = ("date_created",)
    date_hierarchy = "date_created"


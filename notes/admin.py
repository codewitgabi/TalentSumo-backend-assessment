from django.contrib import admin
from .models import Note, SharedNote


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("text", "file", "date_created")
    empty_value_display = "--empty--"
    list_filter = ("date_created",)
    date_hierarchy = "date_created"


@admin.register(SharedNote)
class SharedNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "date_sent")
    empty_value_display = "--empty--"
    date_hierarchy = "date_sent"


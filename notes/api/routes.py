from django.urls import path
from . import views


urlpatterns = [
    path("notes/list/",
        views.NoteListView.as_view(),
        name="notes_list_view"),
    path("note/create/",
        views.NoteCreateView.as_view(),
        name="notes_create_view"),
    path("note/get/<uuid:note_id>/",
        views.NoteDetailView.as_view(),
        name="note_detail_view"),
    path("sharednote/create/",
        views.SharedNoteCreateView.as_view(),
        name="sharednote_create_view"),
    path("sharednote/list/<int:receiver_id>/",
        views.SharedNoteListView.as_view(),
        name="sharednote_list_view"),
]

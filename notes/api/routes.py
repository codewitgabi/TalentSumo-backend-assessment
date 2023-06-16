from django.urls import path
from . import views


urlpatterns = [
    path("notes/list/",
        views.FileListAPIView.as_view(),
        name="notes_list_view"),
    path("notes/create/",
        views.FileCreateAPIView.as_view(),
        name="notes_create_view"),
    path("notes/get/<uuid:note_id>/",
        views.FileDetailAPIView.as_view(),
        name="notes_detail_view"),
]

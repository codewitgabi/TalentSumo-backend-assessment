# external packages imports
from rest_framework import generics

# custom imports
from notes.models import Note
from .serializers import NoteSerializer


class FileListAPIView(generics.ListAPIView):
    """
    Endpoint for listing all uploaded files.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class FileCreateAPIView(generics.CreateAPIView):
    """
    Endpoint for creating new file instances
    """
    serializer_class = NoteSerializer
    model = Note


class FileDetailAPIView(generics.RetrieveAPIView):
    """
    Endpoint to get detail for a particular note.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "note_id"


# external packages imports
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# custom imports
from notes.models import Note, SharedNote
from .serializers import NoteSerializer, SharedNoteSerializer

# user object
User = get_user_model()


class NoteListView(generics.ListAPIView):
    """
    Endpoint for listing all uploaded notes.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NoteCreateView(generics.CreateAPIView):
    """
    Endpoint for creating new note instances
    """
    serializer_class = NoteSerializer
    model = Note


class NoteDetailView(generics.RetrieveAPIView):
    """
    Endpoint to get detail for a particular note.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "note_id"


class SharedNoteCreateView(generics.CreateAPIView):
    """
    Endpoint for sharing note object between users
    """
    serializer_class = SharedNoteSerializer
    model = SharedNote
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class SharedNoteListView(generics.ListAPIView):
    """
    Endpoint for listing all shared notes between two users.
    """
    serializer_class = SharedNoteSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        sender = self.request.user
        receiver = get_object_or_404(User, id=self.kwargs.get("receiver_id"))
        
        sender_sn = SharedNote.objects.filter(sender=sender, receiver=receiver)
        receiver_sn = SharedNote.objects.filter(sender=receiver, receiver=sender)
        
        shared_notes = sender_sn | receiver_sn
        
        return shared_notes.order_by("-date_sent")


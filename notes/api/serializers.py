# external packages imports
from rest_framework import serializers
from django.contrib.auth import get_user_model

# custom imports
from notes.models import Note, SharedNote

# user object
User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    date_created = serializers.SerializerMethodField()
    
    class Meta:
        model = Note
        fields = ("id", "text", "file", "date_created")
    
    
    def validate(self, data):
        """
        Checks if either of text or file.is sent
        """
        if data["text"] == "" and data["file"] is None:
            raise serializers.ValidationError("Both `Text` and `File` fields cannot be empty")
            
        return data;

    def get_date_created(self, obj):
        """
        Format date created representation
        """
        return obj.date_created.strftime("%Y-%m-%d %H:%M %p")


class SharedNoteSerializer(serializers.ModelSerializer):
    date_sent = serializers.SerializerMethodField()
    note = serializers.HyperlinkedRelatedField(
        view_name="note_detail_view",
        queryset=Note.objects.all(), lookup_field="id",
        lookup_url_kwarg="note_id")
    sender = serializers.SerializerMethodField()
    receiver = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    
    class Meta:
        model = SharedNote
        fields = ("id", "sender", "receiver", "note", "date_sent")
        depth = 1
        read_only_fields = ["sender"]
    
    def get_date_sent(self, obj):
        """
        Format date sent representation
        """
        return obj.date_sent.strftime("%Y-%m-%d %H:%M %p")
    
    def get_sender(self, obj):
        """
        Format sender representation.
        """
        return {
            "id": obj.sender.id,
            "username": obj.sender.username
        }

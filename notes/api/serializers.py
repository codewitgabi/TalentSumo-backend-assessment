# external packages imports
from rest_framework import serializers

# custom imports
from notes.models import Note


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
        return obj.date_created.strftime("%Y-%m-%d %H:%M %p")

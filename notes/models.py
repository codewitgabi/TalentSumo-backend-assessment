import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

# user object
User = get_user_model()


class Note(models.Model):
    """
    Database table for storing uploaded and shared notes.
    text: stores textual data; Optional
    file: stores audios and videos; Optional
    
    Note that one of either text or file must be sent; Validations will be provided for that.
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    text = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(["mp3", "mp4", "wav", "avi", "mkv"])])
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_created"]
    
    def clean(self):
        if self.text == "" and self.file.name is None:
            raise ValidationError("Both `Text` and `File` fields cannot be empty")
        super().clean()
    
    def __str__(self):
        return self.text


class SharedNote(models.Model):
    """
    Stores notes shared amongst users
    sender: user object sending the note
    receiver: user object receiving the note
    note: note instance being sent
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note_receiver")
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_sent"]
    
    def __str__(self):
        return str(self.id)


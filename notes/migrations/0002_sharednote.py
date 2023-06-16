# Generated by Django 3.2 on 2023-06-16 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.note')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]
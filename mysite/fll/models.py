from django.db import models


class AudioNote(models.Model):
    audio_hash = models.CharField(max_length=100, blank=True)
    english = models.TextField(blank=True)
    german = models.TextField(blank=True)
    italian = models.TextField(blank=True)
    spanish = models.TextField(blank=True)
    swahili = models.TextField(blank=True)

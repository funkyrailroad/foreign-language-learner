from django.template.response import TemplateResponse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np


from fll.serializers import AudioNoteSerializer
from fll.models import AudioNote
import fll.util as u


def index(request):
    return TemplateResponse(request, "example_app/index.html")


class TranscriptionView(APIView):
    def post(self, request):
        file = request.data["audio"].file
        audio_frame = file.read()
        buffer = np.frombuffer(audio_frame, dtype=np.int16).astype(np.float32) / 32767.0

        text = u.transcribe_audio_with_whisper(buffer)
        return Response({"transcription": text})


class AudioNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio notes to be viewed or edited.
    """

    queryset = AudioNote.objects.all()
    serializer_class = AudioNoteSerializer

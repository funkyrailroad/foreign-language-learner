import os
from uuid import uuid4
from django.template.response import TemplateResponse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from fll.serializers import AudioNoteSerializer
from fll.models import AudioNote
import fll.util as u


def index(request):
    return TemplateResponse(request, "example_app/index.html")


class TranscriptionView(APIView):
    def post(self, request):
        file = request.data["audio"].file
        audio_frame = file.read()

        fn = f"audio-{uuid4()}.wav"
        with open(fn, "wb") as f:
            f.write(audio_frame)
        text = u.transcribe_audio_with_whisper(fn)
        os.remove(fn)

        return Response({"transcription": text})


class AudioNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio notes to be viewed or edited.
    """

    queryset = AudioNote.objects.all()
    serializer_class = AudioNoteSerializer

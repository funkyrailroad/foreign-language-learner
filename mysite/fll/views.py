from django.template.response import TemplateResponse

from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView


import fll.serializers as s
from fll.models import AudioNote
import fll.util as u


def index(request):
    return TemplateResponse(request, "example_app/index.html")


class TranscriptionView(APIView):
    def post(self, request):
        file = request.data["audio"]
        text = u.transcribe_in_memory_uploaded_file(file)
        translations = u.get_translations(text)
        return Response({"transcription": text, **translations})


class AudioNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio notes to be viewed or edited.
    """

    queryset = AudioNote.objects.all()

    def get_serializer_class(self):
        serializer = self.request.query_params.get("serializer")
        if serializer == "hyperlinked":
            return s.AudioNoteHyperlinkedModelSerializer
        if serializer == "custom":
            return s.AudioNoteCustomSerializer

    def create(self, request):
        audio = request.data["audio"]
        english = u.transcribe_in_memory_uploaded_file(audio)
        request.data["audio_hash"] = s.hash_audio_file(audio)
        request.data["english"] = english
        request.data["german"] = u.translate_to_german(english)
        request.data["italian"] = u.translate_to_italian(english)
        request.data["spanish"] = u.translate_to_spanish(english)
        request.data["swahili"] = u.translate_to_swahili(english)
        return super().create(request)

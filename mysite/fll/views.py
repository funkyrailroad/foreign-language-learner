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
        file = request.data["audio"]
        text = u.transcribe_in_memory_uploaded_file(file)
        translations = u.get_translations(text)
        return Response({"transcription": text, **translations})


class AudioNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio notes to be viewed or edited.
    """

    queryset = AudioNote.objects.all()
    serializer_class = AudioNoteSerializer

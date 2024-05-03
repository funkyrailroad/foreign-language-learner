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
    # parser_classes = [FileUploadParser]
    parser_classes = [MultiPartParser]
    # parser_classes = [FormParser]

    def get_serializer_class(self):
        print(self.request.data)
        print(self.request.FILES)
        breakpoint()
        serializer = self.request.query_params.get("serializer")
        if serializer == "hyperlinked":
            return s.AudioNoteHyperlinkedModelSerializer
        if serializer == "custom":
            return s.AudioNoteCustomSerializer

    def post(self, request, *args, **kwargs):
        breakpoint()
        return self.create(request, *args, **kwargs)

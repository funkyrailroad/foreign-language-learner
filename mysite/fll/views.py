from django.template.response import TemplateResponse

from rest_framework import viewsets

from fll.serializers import AudioNoteSerializer
from fll.models import AudioNote


def index(request):
    return TemplateResponse(request, "example_app/index.html")


class AudioNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audio notes to be viewed or edited.
    """

    queryset = AudioNote.objects.all()
    serializer_class = AudioNoteSerializer

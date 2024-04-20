from rest_framework import serializers

from fll.models import AudioNote
import fll.util as u


class AudioNoteSerializer(serializers.HyperlinkedModelSerializer):
    """
    # TODO: make translation fields read-only
    """
    class Meta:
        model = AudioNote
        fields = "__all__"

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
        read_only_fields = ['german', 'italian', 'spanish', 'swahili']

    def create(self, validated_data):
        english = validated_data["english"]
        validated_data['german'] = u.translate_to_german(english)
        validated_data['italian'] = u.translate_to_italian(english)
        validated_data['spanish'] = u.translate_to_spanish(english)
        validated_data['swahili'] = u.translate_to_swahili(english)
        audio_note = AudioNote.objects.create(**validated_data)
        audio_note.save()
        return audio_note

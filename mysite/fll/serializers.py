import hashlib

from rest_framework import serializers

from fll.models import AudioNote
import fll.util as u


class AudioHashField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


class AudioNoteHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    # TODO: make translation fields read-only
    """

    audio_hash = AudioHashField(write_only=True)

    class Meta:
        model = AudioNote
        fields = [
            "audio_hash",
            "english",
            "german",
            "italian",
            "spanish",
            "swahili",
            "url",
        ]


class GermanTranslationField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


class EnglishTranscriptionField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


def hash_audio_file(file):
    the_bytes = file.read()
    return hashlib.sha256(the_bytes).hexdigest()


class AudioNoteCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    audio_hash = AudioHashField(write_only=True)
    english = EnglishTranscriptionField()
    german = GermanTranslationField()
    italian = serializers.CharField()
    spanish = serializers.CharField()
    swahili = serializers.CharField()

    class Meta:
        model = AudioNote
        fields = [
            "english",
            "german",
            "italian",
            "spanish",
            "swahili",
        ]

    def validate_audio_hash(self, value):
        return value

    def create(self, validated_data):
        return AudioNote.objects.create(**validated_data)

import hashlib

from rest_framework import serializers

from fll.models import AudioNote
import fll.util as u


class AudioNoteHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    # TODO: make translation fields read-only
    """

    class Meta:
        model = AudioNote
        fields = [
            "english",
            "german",
            "italian",
            "spanish",
            "swahili",
            "url",
        ]
        read_only_fields = [
            "german",
            "italian",
            "spanish",
            "swahili",
        ]

    def create(self, validated_data):
        english = validated_data["english"]
        validated_data["german"] = u.translate_to_german(english)
        validated_data["italian"] = u.translate_to_italian(english)
        validated_data["spanish"] = u.translate_to_spanish(english)
        validated_data["swahili"] = u.translate_to_swahili(english)
        audio_note = AudioNote.objects.create(**validated_data)
        audio_note.save()
        return audio_note


class AudioHashField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data


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
    english = EnglishTranscriptionField(read_only=True)
    german = GermanTranslationField(read_only=True)
    italian = serializers.CharField(read_only=True)
    spanish = serializers.CharField(read_only=True)
    swahili = serializers.CharField(read_only=True)

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
        audio = validated_data["audio_hash"]
        english = u.transcribe_in_memory_uploaded_file(audio)
        data = {
            "audio_hash": hash_audio_file(audio),
            "english": english,
            "german": u.translate_to_german(english),
            "italian": u.translate_to_italian(english),
            "spanish": u.translate_to_spanish(english),
            "swahili": u.translate_to_swahili(english),
        }
        # TODO: figure out how to validate these translations
        audio_note = AudioNote.objects.create(**data)
        return audio_note

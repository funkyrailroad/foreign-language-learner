from rest_framework import serializers

from fll.models import AudioNote
import fll.util as u


class AudioNoteHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    # TODO: make translation fields read-only
    """

    class Meta:
        model = AudioNote
        fields = "__all__"
        read_only_fields = ["german", "italian", "spanish", "swahili"]

    def create(self, validated_data):
        english = validated_data["english"]
        validated_data["german"] = u.translate_to_german(english)
        validated_data["italian"] = u.translate_to_italian(english)
        validated_data["spanish"] = u.translate_to_spanish(english)
        validated_data["swahili"] = u.translate_to_swahili(english)
        audio_note = AudioNote.objects.create(**validated_data)
        audio_note.save()
        return audio_note


class AudioNoteCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    english = serializers.CharField()
    german = serializers.CharField(read_only=True)
    italian = serializers.CharField(read_only=True)
    spanish = serializers.CharField(read_only=True)
    swahili = serializers.CharField(read_only=True)

    class Meta:
        model = AudioNote
        fields = "__all__"

    def create(self, validated_data):
        english = validated_data["english"]
        data = {
            "german": u.translate_to_german(english),
            "italian": u.translate_to_italian(english),
            "spanish": u.translate_to_spanish(english),
            "swahili": u.translate_to_swahili(english),
        }
        audio_note = AudioNote.objects.create(**validated_data, **data)
        audio_note.save()
        return audio_note

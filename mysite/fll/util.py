import os
import whisper
import translators as ts


def transcribe_audio_with_whisper(fp):
    result = model.transcribe(fp)
    return result["text"].strip()


# model = whisper.load_model("base.en")


def translate_to_german(text):
    return ts.translate_text(text, to_language="de")


def translate_to_italian(text):
    return ts.translate_text(text, to_language="it")


def translate_to_spanish(text):
    return ts.translate_text(text, to_language="es")


def translate_to_swahili(text):
    return ts.translate_text(text, to_language="sw")

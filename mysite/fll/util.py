import os
from uuid import uuid4
from django.core.files.uploadedfile import InMemoryUploadedFile
import whisper
import translators as ts


def transcribe_audio_with_whisper(fp: str):
    # TODO: get this to work with an inmemory uploaded file
    result = model.transcribe(fp)
    return result["text"].strip()


model = whisper.load_model("base.en")


def translate_to_german(text):
    return ts.translate_text(text, to_language="de")


def translate_to_italian(text):
    return ts.translate_text(text, to_language="it")


def translate_to_spanish(text):
    return ts.translate_text(text, to_language="es")


def translate_to_swahili(text):
    return ts.translate_text(text, to_language="sw")


def transcribe_in_memory_uploaded_file(file: InMemoryUploadedFile):
    audio_frame = file.read()
    fn = f"audio-{uuid4()}.wav"
    with open(fn, "wb") as f:
        f.write(audio_frame)
    text = transcribe_audio_with_whisper(fn)
    os.remove(fn)
    return text


def get_translations(text: str) -> dict:
    german = translate_to_german(text)
    italian = translate_to_italian(text)
    spanish = translate_to_spanish(text)
    swahili = translate_to_swahili(text)
    return dict(german=german, italian=italian, spanish=spanish, swahili=swahili)

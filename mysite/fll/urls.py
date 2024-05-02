from django.urls import path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r"audio-notes-hyperlinked", views.AudioNoteHyperlinkedViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", views.index, name="index"),
    path("transcribe/", views.TranscriptionView.as_view()),
]

from django.urls import path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r"audio-notes", views.AudioNoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", views.index, name="index"),
]

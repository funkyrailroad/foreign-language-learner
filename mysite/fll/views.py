from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, "example_app/index.html")

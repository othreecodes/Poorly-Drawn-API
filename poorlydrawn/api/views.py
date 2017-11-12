from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.


class ComicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComicSerializer
    queryset = models.Comic.objects.all()


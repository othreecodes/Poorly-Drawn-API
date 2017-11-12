from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.pagination import PageNumberPagination


# Create your views here.



class ComicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComicSerializer
    queryset = models.Comic.objects.all()
    # lookup_field = 'slug' #TODO: is slug a better thing to use?

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import serializers
from . import models
from rest_framework.pagination import PageNumberPagination


# Create your views here.



class ComicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComicSerializer
    queryset = models.Comic.objects.all()
    permission_classes = [IsAdminUser]
    http_method_names = ['get']
    # lookup_field = 'slug' #TODO: is slug a better thing to use?

    def get_view_description(self, html=False):
        return "Poorly Drawn Lines Unofficial API"



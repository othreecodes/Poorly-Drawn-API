from rest_framework import serializers
from . import models


class ComicSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="comic-detail")

    class Meta:
        model = models.Comic
        fields = ['id', 'url', 'created', 'title', 'link', 'description', 'image', 'slug']
        ordering = "created"

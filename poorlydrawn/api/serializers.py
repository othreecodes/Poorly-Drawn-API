from rest_framework import serializers
from . import models

class ComicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Comic
        fields = ['created','title','link','description','image']

from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

class Comic(TimeStampedModel):
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    description = models.TextField(blank=True,null=True)
    image = models.CharField(max_length=1000,null=True,blank=True)



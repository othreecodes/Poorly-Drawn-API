from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'comics', views.ComicViewSet)
from django.conf.urls import url, include

urlpatterns = [

    url(r'^', include(router.urls))

]

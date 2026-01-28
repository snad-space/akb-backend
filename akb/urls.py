"""akb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from akb import views

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'objects', views.ObjectViewSet)

urlpatterns = [
	re_path(r'^', include(router.urls)),
	re_path(r'^whoami/$', views.whoami, name="whoami"),
	re_path(r'^dumpdata/$', views.dumpdata, name="dumpdata"),
]

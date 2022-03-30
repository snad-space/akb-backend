"""akb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
]

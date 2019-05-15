from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from .views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

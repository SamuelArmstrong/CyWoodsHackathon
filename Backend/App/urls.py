from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import SchoolViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'people', PersonViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
]

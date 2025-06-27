from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.airplane import AirplaneViewSet
from .views.airplane_type import AirplaneTypeViewSet

router = DefaultRouter()
router.register(r"airplanes", AirplaneViewSet, basename="airplane")
router.register(r"airplane_types", AirplaneTypeViewSet, basename="airplane_type")

urlpatterns = [
    path("", include(router.urls)),
]

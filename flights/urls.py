from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.airplane import AirplaneViewSet
from .views.airplane_type import AirplaneTypeViewSet
from .views.airport import AirportViewSet
from .views.crew import CrewViewSet

router = DefaultRouter()
router.register(r"airplanes", AirplaneViewSet, basename="airplane")
router.register(r"airplane_types", AirplaneTypeViewSet, basename="airplane_type")
router.register(r"airports", AirportViewSet, basename="airport")
router.register(r"crews", CrewViewSet, basename="crew")

urlpatterns = [
    path("", include(router.urls)),
]

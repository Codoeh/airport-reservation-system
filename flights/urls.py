from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.airplane import AirplaneViewSet
from .views.airplane_type import AirplaneTypeViewSet
from .views.airport import AirportViewSet
from .views.crew import CrewViewSet
from .views.flight import FlightViewSet
from .views.order import OrderViewSet
from .views.route import RouteViewSet
from .views.ticket import TicketViewSet

router = DefaultRouter()
router.register(r"airplanes", AirplaneViewSet, basename="airplane")
router.register(
    r"airplane_types",
    AirplaneTypeViewSet,
    basename="airplane_type"
)
router.register(r"airports", AirportViewSet, basename="airport")
router.register(r"crews", CrewViewSet, basename="crew")
router.register(r"routes", RouteViewSet, basename="route")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"tickets", TicketViewSet, basename="ticket")
router.register(r"flights", FlightViewSet, basename="flight")

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework import viewsets
from flights.serializers.airport import AirportSerializer
from flights.models.airport import Airport

class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()

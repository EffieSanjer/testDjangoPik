from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from bookings.serializers import BookingCreateSerializer


class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer


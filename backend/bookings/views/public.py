from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookings.serializers import BookingCreateSerializer
from ..tasks import create_booking_task


class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            create_booking_task.delay_on_commit(
                data=serializer.validated_data
            )

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import re

from rest_framework import serializers

from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingListSerializer(BookingSerializer):
    class Meta(BookingSerializer.Meta):
        fields = ['id', 'created_at', 'name', 'phone', 'hike', 'is_canceled']


class BookingCreateSerializer(BookingSerializer):
    class Meta(BookingSerializer.Meta):
        fields = ['name', 'phone', 'email', 'hike']

    def validate_phone(self, value):
        if not re.match(r'^\+7\d{10}$', value.strip()):
            raise serializers.ValidationError("Некорректный номер телефона")
        return value

import re

from rest_framework import serializers

from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingListSerializer(BookingSerializer):
    hike_title = serializers.CharField(source='hike.title')
    hike_slug = serializers.CharField(source='hike.slug')

    class Meta(BookingSerializer.Meta):
        fields = ['id', 'created_at', 'name', 'phone', 'email', 'hike_title', 'hike_slug', 'is_canceled']


class BookingCreateSerializer(BookingSerializer):
    hike_id = serializers.CharField(source='hike.id')

    class Meta(BookingSerializer.Meta):
        fields = ['name', 'phone', 'email', 'hike_id']

    def validate_phone(self, value):
        if not re.match(r'^\+7\d{10}$', value.strip()):
            raise serializers.ValidationError("Некорректный номер телефона")
        return value

    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value.strip()):
            raise serializers.ValidationError("Некорректный email")
        return value

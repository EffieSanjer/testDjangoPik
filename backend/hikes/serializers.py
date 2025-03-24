from rest_framework import serializers

from .models import Hike


class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = '__all__'


class HikeRetrieveSerializer(HikeSerializer):
    class Meta(HikeSerializer.Meta):
        fields = ['id', 'title', 'description', 'start_at', 'image', 'is_public']


class PublicHikeListSerializer(HikeSerializer):
    class Meta(HikeSerializer.Meta):
        fields = ['id', 'title', 'slug', 'image']


class PrivateHikeListSerializer(HikeSerializer):
    class Meta(HikeSerializer.Meta):
        fields = ['id', 'title', 'slug', 'start_at', 'image', 'is_public']


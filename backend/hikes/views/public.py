from django.utils import timezone
from rest_framework.generics import RetrieveAPIView, ListAPIView

from hikes.models import Hike
from hikes.serializers import PublicHikeListSerializer, HikeRetrieveSerializer


class PublicHikeListView(ListAPIView):
    queryset = Hike.objects.filter(is_public=True, start_at__gt=timezone.now())
    serializer_class = PublicHikeListSerializer


class PublicHikeDetailView(RetrieveAPIView):
    queryset = Hike.objects.filter(is_public=True, start_at__gt=timezone.now())
    serializer_class = HikeRetrieveSerializer
    lookup_field = 'slug'




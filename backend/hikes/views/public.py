from rest_framework.generics import RetrieveAPIView, ListAPIView

from hikes.models import Hike
from hikes.serializers import PublicHikeListSerializer, HikeRetrieveSerializer


class PublicHikeListView(ListAPIView):
    queryset = Hike.objects.filter(is_public=True)
    serializer_class = PublicHikeListSerializer


class PublicHikeDetailView(RetrieveAPIView):
    queryset = Hike.objects.filter(is_public=True)
    serializer_class = HikeRetrieveSerializer
    lookup_field = 'slug'




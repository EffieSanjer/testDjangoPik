from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from hikes.models import Hike
from hikes.serializers import HikeRetrieveSerializer, PrivateHikeListSerializer


class PrivateHikeListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hike.objects.all()
    serializer_class = PrivateHikeListSerializer


class PrivateHikeDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hike.objects.all()
    serializer_class = HikeRetrieveSerializer
    lookup_field = 'slug'


class PrivateHikeCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hike.objects.all()
    serializer_class = HikeRetrieveSerializer


class PrivateHikeUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hike.objects.all()
    serializer_class = HikeRetrieveSerializer
    lookup_field = 'slug'

    parser_classes = (MultiPartParser, FormParser)


class PrivateHikeDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hike.objects.all()
    lookup_field = 'slug'

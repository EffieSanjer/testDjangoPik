from django.urls import path

from hikes.views.private import PrivateHikeDeleteView, PrivateHikeUpdateView, PrivateHikeDetailView, \
    PrivateHikeCreateView, PrivateHikeListView
from hikes.views.public import PublicHikeListView, PublicHikeDetailView

urlpatterns = [
    # private
    path('private/hikes/', PrivateHikeListView.as_view(), name='hike-list'),
    path('private/hikes/create/', PrivateHikeCreateView.as_view(), name='hike-create'),
    path('private/hikes/<slug:slug>/', PrivateHikeDetailView.as_view(), name='hike-detail'),
    path('private/hikes/<slug:slug>/update/', PrivateHikeUpdateView.as_view(), name='hike-update'),
    path('private/hikes/<slug:slug>/delete/', PrivateHikeDeleteView.as_view(), name='hike-delete'),

    # public
    path('public/hikes/', PublicHikeListView.as_view(), name='public-hike-list'),
    path('public/hikes/<slug:slug>/', PublicHikeDetailView.as_view(), name='public-hike-detail')

]

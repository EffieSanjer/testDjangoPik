from django.urls import path

from bookings.views.private import BookingListView, BookingCancelView
from bookings.views.public import BookingCreateView

urlpatterns = [
    # public
    path('public/bookings/create/', BookingCreateView.as_view(), name='booking-create'),

    # private
    path('private/bookings/', BookingListView.as_view(), name='booking-list'),
    path('private/bookings/<int:pk>/cancel/', BookingCancelView.as_view(), name='booking-cancel')
]

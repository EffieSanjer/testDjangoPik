from time import sleep

from celery import shared_task

from .models import Booking


@shared_task
def create_booking_task(data):
    sleep(5)

    booking = Booking.objects.create(
        hike_id=data['hike']['id'],
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )

    return booking.id

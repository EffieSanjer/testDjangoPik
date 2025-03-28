import random
from datetime import timedelta

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from django.utils import timezone
from faker import Faker

from bookings.models import Booking
from hikes.models import Hike

faker = Faker('ru_RU')


class Command(BaseCommand):
    def __generate_booking(self, hike):
        phone_digits = [str(random.randint(0, 9)) for _ in range(9)]

        Booking.objects.create(
            hike=hike,
            name=faker.name(),
            phone='+79' + ''.join(phone_digits),
            email=faker.email(),
        )

    def __generate_hike(self, idx):
        hike = Hike(
            title=f"Поход {idx}",
            description=faker.text(max_nb_chars=255),
            start_at=timezone.now() + timedelta(days=random.randint(1, 365)),
            is_public=random.choice([True, False])
        )
        hike.save()

        try:
            random_image = requests.get('https://lipsum.app/random/1200x650', allow_redirects=True)
            random_image.raise_for_status()

            hike.image.save(
                f'hike_{idx}.jpg',
                ContentFile(random_image.content),
                save=True
            )
        except Exception as e:
            print(e)

        for _ in range(random.randint(0, 5)):
            self.__generate_booking(hike)

    def handle(self, *args, **options):

        if not Hike.objects.exists():
            for idx in range(10):
                self.__generate_hike(idx)


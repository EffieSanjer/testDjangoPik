import random
from datetime import timedelta

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from django.utils import timezone
from faker import Faker

from bookings.models import Booking
from hikes.models import Hike


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(10):
            hike = Hike(
                title=faker.sentence(nb_words=2),
                description=faker.text(max_nb_chars=255),
                start_at=timezone.now() + timedelta(days=random.randint(1, 365)),
                is_public=random.choice([True, False])
            )
            hike.save()

            try:
                random_image = requests.get('https://lipsum.app/random/1200x650', allow_redirects=True)
                random_image.raise_for_status()

                hike.image.save(
                    f'hike_{_}.jpg',
                    ContentFile(random_image.content),
                    save=True
                )
            except Exception as e:
                print(e)

            for _ in range(random.randint(0, 5)):
                phone_digits = [str(random.randint(0, 9)) for _ in range(10)]

                Booking.objects.create( 
                    hike=hike,
                    name=faker.name(),
                    phone='+7' + ''.join(phone_digits),
                    email=faker.email(),
                )


from django.db import models
from django.db.models.functions import Now

from hikes.models import Hike


class Booking(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=16)
    email = models.EmailField('Email')
    created_at = models.DateTimeField('Дата создания', db_default=Now())

    hike = models.ForeignKey(Hike, on_delete=models.CASCADE, verbose_name='Поход', related_name='bookings')
    is_canceled = models.BooleanField('Отменена', default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{str(self.id)} - {self.hike.title}"

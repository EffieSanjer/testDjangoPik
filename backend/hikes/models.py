from django.db import models
from django.db.models.functions import Now
from django.utils.text import slugify


class Hike(models.Model):
    title = models.CharField('Название похода', max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField('Краткое описание', blank=True, null=True)
    start_at = models.DateTimeField('Дата и время похода', db_default=Now())
    image = models.ImageField('Фото', upload_to='hikes/', blank=True, null=True)
    is_public = models.BooleanField('Показывать на сайте', default=True)

    class Meta:
        ordering = ['start_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

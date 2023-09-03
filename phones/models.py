from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.URLField()
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.price};" \
               f" {self.image};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"
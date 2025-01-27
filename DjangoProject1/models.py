# models.py

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.IntegerField()
    imageSrc = models.URLField()

    def __str__(self):
        return self.title

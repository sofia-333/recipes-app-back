from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    time_to_prepare = models.IntegerField()
    # image = models.ImageField()

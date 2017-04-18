from django.db import models
from userauth.models import User


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=60)
    weight = models.PositiveSmallIntegerField(default=60)
    age = models.PositiveSmallIntegerField(default=20)
    level = models.PositiveSmallIntegerField(default=1)


class Campaign(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ManyToManyField(Character)

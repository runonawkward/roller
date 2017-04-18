from django.db import models
from userauth.models import User


class ClassFeature(models.Model):
    feature_name = models.CharField(max_length=100, primary_key=True)


class Class(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    features = models.ManyToManyField(ClassFeature)


class Ability(models.Model):
    name = models.CharField(max_length=20, primary_key=True)


class Feat(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    ancestors = models.ManyToManyField('self', related_name='ancestors', blank=True)
    children = models.ManyToManyField('self', related_name='children', blank=True)
    class_features = models.ManyToManyField(ClassFeature)


class AbilityRequirement(models.Model):
    name = models.ForeignKey(Ability, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=12)
    feat_id = models.ForeignKey(Feat, related_name='feat_id', blank=True)


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=60)
    weight = models.PositiveSmallIntegerField(default=60)
    age = models.PositiveSmallIntegerField(default=20)
    feats = models.ManyToManyField(Feat)


class CharacterAbility(models.Model):
    name = models.ForeignKey(Ability, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(default=7)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)


class CharacterClass(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1)
    primary = models.BooleanField()


class Campaign(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ManyToManyField(Character)
    description = models.CharField(max_length=100, null=True, blank=True)

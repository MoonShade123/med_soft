from django.db import models

from med_app.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=25, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=25, blank=True)
    birth_date = models.DateTimeField(blank=False)
    weight = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    country = models.CharField(blank=True, max_length=25)
    med_ensurance = models.BooleanField(default=False)
    sex = models.CharField(blank=False, max_length=20, default='Unknown')

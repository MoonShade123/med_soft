from datetime import date

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
    birth_date = models.DateField(blank=False)
    weight = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    country = models.CharField(blank=True, max_length=25)
    med_insurance = models.BooleanField(default=False)
    sex = models.CharField(blank=False, max_length=20, default='Unknown')

    def __str__(self):
        return self.name

    def calculate_age(self):
        today = date.today()

        try:
            birthday = self.birth_date.replace(year=today.year)
        # raised when birth date is February 29 and the current year is not a leap year
        except ValueError:
            birthday = self.birth_date.replace(year=today.year, day=self.birth_date.day - 1)

        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year

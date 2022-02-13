from django.db import models

from med_app.models import User


class Blood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    red_blood_cells = models.CharField(max_length=50, blank=False)
    hemoglobin = models.CharField(max_length=50, blank=False)
    white_blood_cells = models.CharField(max_length=50, blank=False)
    color_index = models.CharField(max_length=50, blank=False)
    hematocrit = models.CharField(max_length=50, blank=False)
    reticulocytes = models.CharField(max_length=50, blank=False)
    platelets = models.CharField(max_length=50, blank=False)
    esr = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user

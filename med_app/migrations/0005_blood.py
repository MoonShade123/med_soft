# Generated by Django 4.0.2 on 2022-02-12 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0004_profile_country_profile_med_ensurance_profile_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_blood_cells', models.CharField(max_length=50)),
                ('hemoglobin', models.CharField(max_length=50)),
                ('white_blood_cells', models.CharField(max_length=50)),
                ('color_index', models.CharField(max_length=50)),
                ('hematocrit', models.CharField(max_length=50)),
                ('reticulocytes', models.CharField(max_length=50)),
                ('platelets', models.CharField(max_length=50)),
                ('esr', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
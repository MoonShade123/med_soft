# Generated by Django 4.0.2 on 2022-02-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0003_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='med_ensurance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0008_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.CharField(max_length=3),
        ),
    ]

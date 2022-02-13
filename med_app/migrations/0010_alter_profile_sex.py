# Generated by Django 4.0.2 on 2022-02-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0009_alter_profile_height_alter_profile_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('N', 'Neutral'), ('M', 'Male'), ('F', 'Female')], default='N', max_length=1),
        ),
    ]
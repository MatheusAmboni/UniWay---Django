# Generated by Django 2.2.5 on 2023-12-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_car_review_ride_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Ride',
        ),
    ]

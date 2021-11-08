# Generated by Django 3.2.7 on 2021-10-21 10:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20211012_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 10, 15, 31, 577656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='time_of_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 10, 15, 31, 577536, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='generalinstruction',
            name='instruction',
            field=models.TextField(max_length=1200),
        ),
    ]

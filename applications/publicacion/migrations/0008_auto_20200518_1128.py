# Generated by Django 3.0.6 on 2020-05-18 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0007_auto_20200518_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avisos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 18, 14, 28, 12, 213647, tzinfo=utc)),
        ),
    ]
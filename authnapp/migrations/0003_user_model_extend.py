# Generated by Django 3.2.9 on 2022-04-16 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_user_model_extend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 15, 1, 2, 205037, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]

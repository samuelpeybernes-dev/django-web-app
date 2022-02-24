# Generated by Django 4.0.2 on 2022-02-24 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('HR', 'Hard Rock')], default='HH', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2005, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
            preserve_default=False,
        ),
    ]

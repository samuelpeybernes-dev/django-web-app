# Generated by Django 4.0.2 on 2022-02-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_title_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('HR', 'Hard Rock'), ('CL', 'Classic')], max_length=5),
        ),
    ]

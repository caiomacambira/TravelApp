# Generated by Django 4.0.6 on 2022-07-14 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='name',
            new_name='nome',
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-01 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='destinations',
            new_name='destination',
        ),
    ]
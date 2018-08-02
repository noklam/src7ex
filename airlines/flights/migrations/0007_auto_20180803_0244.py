# Generated by Django 2.1 on 2018-08-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]

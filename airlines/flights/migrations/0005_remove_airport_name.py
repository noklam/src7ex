# Generated by Django 2.0.7 on 2018-08-02 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20180801_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='name',
        ),
    ]

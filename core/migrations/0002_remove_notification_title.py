# Generated by Django 2.0.3 on 2018-03-31 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='title',
        ),
    ]
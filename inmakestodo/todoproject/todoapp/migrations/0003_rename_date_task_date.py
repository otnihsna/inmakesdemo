# Generated by Django 3.2.3 on 2021-05-19 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210519_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='Date',
        ),
    ]
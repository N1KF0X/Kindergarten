# Generated by Django 4.1.4 on 2023-06-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childapplication',
            name='age',
        ),
    ]
# Generated by Django 4.2.10 on 2024-02-12 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelTable(
            name='person',
            table='hms_main_person',
        ),
    ]
# Generated by Django 2.2 on 2020-12-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.CharField(max_length=200),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udharo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
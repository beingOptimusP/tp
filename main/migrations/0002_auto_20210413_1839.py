# Generated by Django 3.1.7 on 2021-04-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userd',
            name='interest',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='userd',
            name='Holdings',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='userd',
            name='wallet',
            field=models.FloatField(default=0),
        ),
    ]
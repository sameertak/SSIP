# Generated by Django 3.2.6 on 2022-10-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_auto_20221006_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='email',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
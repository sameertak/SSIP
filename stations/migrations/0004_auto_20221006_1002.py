# Generated by Django 3.2.6 on 2022-10-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_alter_stationmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='email',
            field=models.CharField(blank=True, default='admin@admin.com', max_length=20),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='subdivision',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

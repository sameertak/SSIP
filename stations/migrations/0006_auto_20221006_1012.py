# Generated by Django 3.2.6 on 2022-10-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_alter_stationmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='contact',
            field=models.CharField(default='079-', max_length=12),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='district',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

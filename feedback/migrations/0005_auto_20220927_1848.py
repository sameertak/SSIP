# Generated by Django 3.2.6 on 2022-09-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_responsemodel_res3'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsemodel',
            name='city',
            field=models.CharField(blank=True, default='NaN', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='responsemodel',
            name='ip_address',
            field=models.CharField(default='0.0.0.0', max_length=30),
        ),
        migrations.AddField(
            model_name='responsemodel',
            name='lat_lng',
            field=models.CharField(blank=True, default='NaN', max_length=30, null=True),
        ),
    ]
# Generated by Django 3.2.6 on 2022-09-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_remove_phonemodel_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.2.6 on 2022-09-25 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_responsemodel_form_id'),
        ('verification', '0013_phonemodel_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.responsemodel'),
        ),
    ]

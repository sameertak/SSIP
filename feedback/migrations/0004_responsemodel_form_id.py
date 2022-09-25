# Generated by Django 3.2.6 on 2022-09-25 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0012_alter_phonemodel_created_at'),
        ('feedback', '0003_alter_responsemodel_res4'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsemodel',
            name='form_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='verification.phonemodel'),
        ),
    ]

# Generated by Django 3.2 on 2022-04-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universeinfotech_app', '0022_missionvission_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionvission',
            name='object_type',
            field=models.CharField(choices=[('mission', 'mission'), ('vission', 'vission')], max_length=150),
        ),
    ]
# Generated by Django 3.2 on 2022-04-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universeinfotech_app', '0021_it_profile_missionvission_news_and_evenet_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionvission',
            name='object_type',
            field=models.CharField(blank=True, choices=[('mission', 'mission'), ('vission', 'vission')], max_length=150),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-12 11:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0021_workexperience_achievements_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workexperience",
            name="achievements",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=80), size=None
            ),
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="skills",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=20), size=None
            ),
        ),
    ]

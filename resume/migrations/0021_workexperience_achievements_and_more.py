# Generated by Django 4.2.6 on 2023-10-12 11:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0020_rename_skill_workexperience_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="workexperience",
            name="achievements",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, default=[], max_length=80),
                default=[],
                size=None,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="skills",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, default=[], max_length=20),
                size=None,
            ),
        ),
        migrations.DeleteModel(
            name="Achievement",
        ),
    ]

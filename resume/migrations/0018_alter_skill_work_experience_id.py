# Generated by Django 4.2.2 on 2023-10-07 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0017_rename_description_workexperience_responsibility_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="work_experience_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="skills",
                to="resume.workexperience",
            ),
        ),
    ]

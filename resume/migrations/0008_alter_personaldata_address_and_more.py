# Generated by Django 4.2.2 on 2023-09-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0007_remove_profile_photo_profile_photo_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personaldata",
            name="address",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="personaldata",
            name="date_of_birth",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="personaldata",
            name="first_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="personaldata",
            name="last_name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

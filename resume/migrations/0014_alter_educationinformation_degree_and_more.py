# Generated by Django 4.2.2 on 2023-10-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0013_alter_workexperience_company_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationinformation",
            name="degree",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="educationinformation",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="educationinformation",
            name="institution",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="educationinformation",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
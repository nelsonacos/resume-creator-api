# Generated by Django 4.2.2 on 2023-09-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0010_alter_contactdata_email_alter_contactdata_github_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdata",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-29 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='profile_photos/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('company_description', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('skills', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_description', to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_data', to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency', models.CharField(choices=[('N', 'Nativo'), ('P', 'Principiante'), ('B', 'Básico'), ('I', 'Intermedio'), ('A', 'Avanzado'), ('F', 'Fluente')], max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='EducationInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_information', to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_data', to='resume.profile')),
            ],
        ),
    ]

from django.db import models


class Profile(models.Model):
    photo_url = models.URLField(blank=True)
    title = models.CharField(max_length=100)


class PersonalData(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="personal_data"
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)


class ContactData(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="contact_data"
    )
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)


class ProfileDescription(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="profile_description"
    )
    summary = models.TextField(blank=True)


class WorkExperience(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="work_experiences"
    )
    company = models.CharField(max_length=100, blank=True)
    company_description = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    skills = models.TextField(blank=True)


class EducationInformation(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="education_information"
    )
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)


class Language(models.Model):
    PROFICIENCY_CHOICES = (
        ("N", "Nativo"),
        ("P", "Principiante"),
        ("B", "Básico"),
        ("I", "Intermedio"),
        ("A", "Avanzado"),
        ("F", "Fluente"),
    )

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="languages"
    )
    name = models.CharField(max_length=100, blank=True)
    proficiency = models.CharField(
        max_length=1, blank=True, choices=PROFICIENCY_CHOICES
    )

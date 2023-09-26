from django.db import models


class Profile(models.Model):
    photo = models.ImageField(upload_to="profile_photos/", blank=True)
    title = models.CharField(max_length=100)


class PersonalData(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="personal_data"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)


class ContactData(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="contact_data"
    )
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()


class ProfileDescription(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="profile_description"
    )
    summary = models.TextField()


class WorkExperience(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="work_experiences"
    )
    company = models.CharField(max_length=100)
    company_description = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    skills = models.TextField()


class EducationInformation(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="education_information"
    )
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


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
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=1, choices=PROFICIENCY_CHOICES)

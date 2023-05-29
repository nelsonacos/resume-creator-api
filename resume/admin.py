from django.contrib import admin
from .models import Profile, PersonalData, ContactData, ProfileDescription, WorkExperience, EducationInformation, Language

admin.site.register(Profile)
admin.site.register(PersonalData)
admin.site.register(ContactData)
admin.site.register(ProfileDescription)
admin.site.register(WorkExperience)
admin.site.register(EducationInformation)
admin.site.register(Language)

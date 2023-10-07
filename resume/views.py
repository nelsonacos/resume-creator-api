from rest_framework import viewsets
from .models import (
    Profile,
    PersonalData,
    ContactData,
    ProfileDescription,
    Achievement,
    WorkExperience,
    EducationInformation,
    Language,
)
from .serializers import (
    ProfileSerializer,
    PersonalDataSerializer,
    ContactDataSerializer,
    ProfileDescriptionSerializer,
    AchievementSerializer,
    WorkExperienceSerializer,
    EducationInformationSerializer,
    LanguageSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PersonalDataViewSet(viewsets.ModelViewSet):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer


class ContactDataViewSet(viewsets.ModelViewSet):
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer


class ProfileDescriptionViewSet(viewsets.ModelViewSet):
    queryset = ProfileDescription.objects.all()
    serializer_class = ProfileDescriptionSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class EducationInformationViewSet(viewsets.ModelViewSet):
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

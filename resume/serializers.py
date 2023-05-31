from rest_framework import serializers
from .models import Profile, PersonalData, ContactData, ProfileDescription, WorkExperience, EducationInformation, Language

class LanguageSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = Language
        exclude = ['id']

class EducationInformationSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = EducationInformation
        exclude = ['id']

class WorkExperienceSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = WorkExperience
        exclude = ['id']

class ProfileDescriptionSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = ProfileDescription
        exclude = ['id']

class ContactDataSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = ContactData
        exclude = ['id']

class PersonalDataSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)

    class Meta:
        model = PersonalData
        exclude = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer(required=False)
    contact_data = ContactDataSerializer(required=False)
    profile_description = ProfileDescriptionSerializer(required=False)
    work_experiences = WorkExperienceSerializer(many=True, required=False)
    education_information = EducationInformationSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = '__all__'
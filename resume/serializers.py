from rest_framework import serializers
from .models import (
    Profile,
    PersonalData,
    ContactData,
    ProfileDescription,
    WorkExperience,
    EducationInformation,
    Language,
)


class LanguageSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = Language
        fields = "__all__"


class EducationInformationSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = EducationInformation
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = WorkExperience
        fields = "__all__"


class ProfileDescriptionSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = ProfileDescription
        fields = "__all__"


class ContactDataSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = ContactData
        fields = "__all__"


class PersonalDataSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = PersonalData
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer(required=False)
    contact_data = ContactDataSerializer(required=False)
    profile_description = ProfileDescriptionSerializer(required=False)
    work_experiences = WorkExperienceSerializer(many=True, required=False)
    education_information = EducationInformationSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = "__all__"

from django.test import TestCase
from resume.models import Profile
from resume.serializers import (
    LanguageSerializer,
    EducationInformationSerializer,
    WorkExperienceSerializer,
    ProfileDescriptionSerializer,
    ContactDataSerializer,
    PersonalDataSerializer,
    ProfileSerializer,
)


class LanguageSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_language_serializer_valid_data(self):
        language_data = {
            "profile": self.profile.id,
            "name": "English",
            "proficiency": "F",
        }
        serializer = LanguageSerializer(data=language_data)
        self.assertTrue(serializer.is_valid())

    def test_language_serializer_missing_required_fields(self):
        language_data = {
            "name": "English",
            "proficiency": "F",
        }
        serializer = LanguageSerializer(data=language_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)

    def test_language_serializer_invalid_proficiency(self):
        language_data = {
            "profile": self.profile.id,
            "name": "English",
            "proficiency": "X",
        }
        serializer = LanguageSerializer(data=language_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("proficiency", serializer.errors)

    def test_language_serializer_empty_data(self):
        language_data = {}
        serializer = LanguageSerializer(data=language_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)
        self.assertIn("name", serializer.errors)
        self.assertIn("proficiency", serializer.errors)


class EducationInformationSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_education_information_serializer_valid_data(self):
        education_data = {
            "profile": self.profile.id,
            "degree": "Bachelor of Science",
            "institution": "University of Example",
            "start_date": "2018-09-01",
            "end_date": "2022-06-30",
            "description": "Studied Computer Science",
        }
        serializer = EducationInformationSerializer(data=education_data)
        self.assertTrue(serializer.is_valid())

    def test_education_information_serializer_missing_required_fields(self):
        education_data = {
            "degree": "Bachelor of Science",
            "institution": "University of Example",
        }
        serializer = EducationInformationSerializer(data=education_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)
        self.assertIn("start_date", serializer.errors)

    def test_education_information_serializer_empty_data(self):
        education_data = {}
        serializer = EducationInformationSerializer(data=education_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)
        self.assertIn("degree", serializer.errors)
        self.assertIn("institution", serializer.errors)
        self.assertIn("start_date", serializer.errors)


class WorkExperienceSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_work_experience_serializer_valid_data(self):
        work_experience_data = {
            "profile": self.profile.id,
            "company": "ABC Company",
            "company_description": "A leading software development company",
            "position": "Senior Developer",
            "start_date": "2022-01-01",
            "end_date": "2022-12-31",
            "description": "Worked on various projects using Python and Django",
            "skills": "Python, Django, SQL",
        }
        serializer = WorkExperienceSerializer(data=work_experience_data)
        self.assertTrue(serializer.is_valid())

    def test_work_experience_serializer_missing_required_fields(self):
        work_experience_data = {
            "profile": self.profile.id,
            "company": "ABC Company",
        }
        serializer = WorkExperienceSerializer(data=work_experience_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("position", serializer.errors)
        self.assertIn("start_date", serializer.errors)

    def test_work_experience_serializer_empty_data(self):
        work_experience_data = {}
        serializer = WorkExperienceSerializer(data=work_experience_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)
        self.assertIn("company", serializer.errors)
        self.assertIn("position", serializer.errors)
        self.assertIn("start_date", serializer.errors)


class ProfileDescriptionSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_profile_description_serializer_valid_data(self):
        profile_description_data = {
            "profile": self.profile.id,
            "summary": "Experienced developer with expertise in Python and Django",
        }
        serializer = ProfileDescriptionSerializer(data=profile_description_data)
        self.assertTrue(serializer.is_valid())

    def test_profile_description_serializer_missing_required_fields(self):
        profile_description_data = {
            "profile": self.profile.id,
        }
        serializer = ProfileDescriptionSerializer(data=profile_description_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("summary", serializer.errors)

    def test_profile_description_serializer_empty_data(self):
        profile_description_data = {}
        serializer = ProfileDescriptionSerializer(data=profile_description_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)
        self.assertIn("summary", serializer.errors)


class ContactDataSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_contact_data_serializer_valid_data(self):
        contact_data = {
            "profile": self.profile.id,
            "phone_number": "1234567890",
            "email": "nelson@example.com",
            "website": "https://www.example.com",
            "linkedin": "https://www.linkedin.com/in/desarrolladorpython",
            "github": "https://www.github.com/nelsonacos",
        }
        serializer = ContactDataSerializer(data=contact_data)
        self.assertTrue(serializer.is_valid())

    def test_contact_data_serializer_optional_fields(self):
        contact_data = {
            "profile": self.profile.id,
        }
        serializer = ContactDataSerializer(data=contact_data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn("phone_number", serializer.errors)
        self.assertNotIn("email", serializer.errors)
        self.assertNotIn("website", serializer.errors)
        self.assertNotIn("linkedin", serializer.errors)
        self.assertNotIn("github", serializer.errors)

    def test_contact_data_serializer_empty_data(self):
        contact_data = {}
        serializer = ContactDataSerializer(data=contact_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("profile", serializer.errors)


class PersonalDataSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_personal_data_serializer_valid_data(self):
        personal_data = {
            "profile": self.profile.id,
            "first_name": "Nelson",
            "last_name": "Acosta",
            "date_of_birth": "1990-01-01",
            "address": "123 Main St",
            "city": "New York",
            "country": "USA",
        }
        serializer = PersonalDataSerializer(data=personal_data)
        self.assertTrue(serializer.is_valid())

    def test_personal_data_serializer_optional_fields(self):
        personal_data = {
            "profile": self.profile.id,
        }
        serializer = PersonalDataSerializer(data=personal_data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn("first_name", serializer.errors)
        self.assertNotIn("last_name", serializer.errors)
        self.assertNotIn("date_of_birth", serializer.errors)
        self.assertNotIn("address", serializer.errors)

    def test_personal_data_serializer_empty_data(self):
        personal_data = {}
        serializer = PersonalDataSerializer(data=personal_data)
        self.assertFalse(serializer.is_valid())


class ProfileSerializerTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")

    def test_profile_serializer_with_nested_serializers(self):
        personal_data = {
            "profile": self.profile.id,
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "1990-01-01",
            "address": "123 Main St",
        }
        contact_data = {
            "profile": self.profile.id,
            "phone_number": "1234567890",
            "email": "nelson.acosta@example.com",
            "website": "https://example.com",
            "linkedin": "https://linkedin.com/in/desarrolladorpython",
            "github": "https://github.com/nelsonacos",
        }
        profile_description = {
            "profile": self.profile.id,
            "summary": "Experienced developer with expertise in web development.",
        }
        work_experiences = [
            {
                "profile": self.profile.id,
                "company": "ABC Inc.",
                "company_description": "Software development company",
                "position": "Software Engineer",
                "start_date": "2018-01-01",
                "end_date": "2021-12-31",
                "description": "Worked on various web projects.",
                "skills": "Python, Django, JavaScript",
            },
            {
                "profile": self.profile.id,
                "company": "XYZ Corp.",
                "company_description": "Technology solutions provider",
                "position": "Senior Developer",
                "start_date": "2022-01-01",
                "description": "Leading development team.",
                "skills": "Python, Django, React",
            },
        ]
        education_information = [
            {
                "profile": self.profile.id,
                "degree": "Bachelor of Science",
                "institution": "University of Example",
                "start_date": "2014-01-01",
                "end_date": "2018-12-31",
                "description": "Studied Computer Science.",
            },
        ]
        languages = [
            {
                "profile": self.profile.id,
                "name": "English",
                "proficiency": "F",
            },
            {
                "profile": self.profile.id,
                "name": "Spanish",
                "proficiency": "N",
            },
        ]
        profile_data = {
            "title": "Developer",
            "personal_data": personal_data,
            "contact_data": contact_data,
            "profile_description": profile_description,
            "work_experiences": work_experiences,
            "education_information": education_information,
            "languages": languages,
        }
        serializer = ProfileSerializer(data=profile_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

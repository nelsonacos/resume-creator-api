from django.test import TestCase
from django.core.exceptions import ValidationError
from resume.models import (
    Profile,
    PersonalData,
    ContactData,
    ProfileDescription,
    WorkExperience,
    Achievement,
    EducationInformation,
    Language,
)


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.profile_data = {
            "title": "Developer",
        }

    def test_profile_creation(self):
        # Test creating a profile with values ​​for required fields
        profile = Profile.objects.create(**self.profile_data)

        self.assertEqual(profile.title, "Developer")

    def test_profile_creation_with_missing_required_fields(self):
        # Test creating a profile without providing values ​​for required fields
        profile_data = {}

        profile = Profile(**profile_data)

        with self.assertRaises(ValidationError):
            profile.full_clean()


class PersonalDataModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.personal_data_data = {
            "profile_id": self.profile,
            "first_name": "Nelson",
            "last_name": "Acosta",
            "date_of_birth": "1990-01-01",
            "address": "123 Main St",
        }

    def test_personal_data_creation(self):
        # Test creating a personal_data with values ​​for required fields
        personal_data = PersonalData.objects.create(**self.personal_data_data)

        self.assertEqual(personal_data.profile_id, self.profile)
        self.assertEqual(personal_data.first_name, "Nelson")
        self.assertEqual(personal_data.last_name, "Acosta")
        self.assertEqual(str(personal_data.date_of_birth), "1990-01-01")
        self.assertEqual(personal_data.address, "123 Main St")

    def test_personal_data_creation_with_missing_required_fields(self):
        # Test creating a personal_data without providing values ​​for required fields
        personal_data_data = {}

        personal_data = PersonalData(**personal_data_data)

        with self.assertRaises(ValidationError):
            personal_data.full_clean()


class ContactDataModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.contact_data_data = {
            "profile_id": self.profile,
            "phone_number": "1234567890",
            "email": "nelson@example.com",
            "website": "http://example.com",
            "linkedin": "https://www.linkedin.com/in/desarrolladorpython",
            "github": "https://github.com/nelsonacos",
        }

    def test_contact_data_creation(self):
        # Test creating a contact_data with values ​​for required fields
        contact_data = ContactData.objects.create(**self.contact_data_data)

        self.assertEqual(contact_data.profile_id, self.profile)
        self.assertEqual(contact_data.phone_number, "1234567890")
        self.assertEqual(contact_data.email, "nelson@example.com")
        self.assertEqual(contact_data.website, "http://example.com")
        self.assertEqual(
            contact_data.linkedin, "https://www.linkedin.com/in/desarrolladorpython"
        )
        self.assertEqual(contact_data.github, "https://github.com/nelsonacos")

    def test_contact_data_creation_with_only_required_fields(self):
        # Test creating a contact_data with only the required field "profile"
        contact_data_data = {
            "profile_id": self.profile,
        }
        contact_data = ContactData(**contact_data_data)
        # This should not raise a ValidationError, as only the "profile" field is required
        contact_data.full_clean()


class ProfileDescriptionModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.profile_description_data = {
            "profile_id": self.profile,
            "summary": "Experienced developer with a passion for coding.",
        }

    def test_profile_description_creation(self):
        # Test creating a profile_description with values ​​for required fields
        profile_description = ProfileDescription.objects.create(
            **self.profile_description_data
        )

        self.assertEqual(profile_description.profile_id, self.profile)
        self.assertEqual(
            profile_description.summary,
            "Experienced developer with a passion for coding.",
        )

    def test_profile_description_creation_with_only_required_fields(self):
        # Test creating a profile_description with only the required field "profile"
        profile_description_data = {
            "profile_id": self.profile,
        }

        profile_description = ProfileDescription(**profile_description_data)

        profile_description.full_clean()


class WorkExperienceModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.work_experience_data = {
            "profile_id": self.profile,
            "company": "ABC Company",
            "company_description": "A leading software development company",
            "position": "Senior Developer",
            "start_date": "2022-01-01",
            "responsibility": "Worked on various projects using Python and Django",
            "skills": "Python, Django, SQL",
        }

    def test_work_experience_creation(self):
        # Test creating a work_experience with all values
        work_experience = WorkExperience.objects.create(**self.work_experience_data)

        self.assertEqual(work_experience.profile_id, self.profile)
        self.assertEqual(work_experience.company, "ABC Company")
        self.assertEqual(
            work_experience.company_description,
            "A leading software development company",
        )
        self.assertEqual(work_experience.position, "Senior Developer")
        self.assertEqual(str(work_experience.start_date), "2022-01-01")
        self.assertIsNone(work_experience.end_date)
        self.assertEqual(
            work_experience.responsibility,
            "Worked on various projects using Python and Django",
        )
        self.assertEqual(work_experience.skills, "Python, Django, SQL")

    def test_work_experience_creation_with_only_required_fields(self):
        # Test creating a work_experience with only the required field "profile"
        work_experience_data = {
            "profile_id": self.profile,
        }

        work_experience = WorkExperience(**work_experience_data)
        work_experience.full_clean()


class AchievementModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.work_experience = WorkExperience.objects.create(
            profile_id=self.profile,
            company="ABC Company",
            company_description="A leading software development company",
            position="Senior Developer",
            start_date="2022-01-01",
            responsibility="Worked on various projects using Python and Django",
            skills="Python, Django, SQL",
        )
        self.achievement_data = {
            "work_experience_id": self.work_experience,
            "achievement_text": "Developed a high-impact feature for a client project",
        }

    def test_achievement_creation(self):
        # Test creating an achievement with all values
        achievement = Achievement.objects.create(**self.achievement_data)

        self.assertEqual(achievement.work_experience_id, self.work_experience)
        self.assertEqual(
            achievement.achievement_text,
            "Developed a high-impact feature for a client project",
        )

    def test_achievement_creation_with_only_required_fields(self):
        # Test creating an achievement with only the required field "work_experience_id"
        achievement_data = {
            "work_experience_id": self.work_experience,
        }

        achievement = Achievement(**achievement_data)
        achievement.full_clean()

    def test_achievement_text_max_length(self):
        # Test the maximum length of the achievement_text field
        achievement_text = "A" * 100  # Exceeds the maximum length of 80 characters

        achievement = Achievement(achievement_text=achievement_text)

        with self.assertRaises(ValidationError):
            achievement.full_clean()


class EducationInformationModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.education_data = {
            "profile_id": self.profile,
            "degree": "Bachelor of Science",
            "institution": "University of Example",
            "start_date": "2018-09-01",
            "end_date": "2022-06-30",
            "description": "Studied Computer Science",
        }

    def test_education_information_creation(self):
        # Test creating a education_information with values ​​for required fields
        education_info = EducationInformation.objects.create(**self.education_data)

        self.assertEqual(education_info.profile_id, self.profile)
        self.assertEqual(education_info.degree, "Bachelor of Science")
        self.assertEqual(education_info.institution, "University of Example")
        self.assertEqual(str(education_info.start_date), "2018-09-01")
        self.assertEqual(str(education_info.end_date), "2022-06-30")
        self.assertEqual(education_info.description, "Studied Computer Science")

    def test_education_information_creation_with_only_required_fields(self):
        # Test creating a education_information with only the required field "profile"
        education_information_data = {
            "profile_id": self.profile,
        }

        education_information = EducationInformation(**education_information_data)
        education_information.full_clean()


class LanguageModelTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(title="Developer")
        self.language_data = {
            "profile_id": self.profile,
            "name": "Spanish",
            "proficiency": "N",
        }

    def test_language_creation(self):
        # Test creating a language with values ​​for required fields
        language = Language.objects.create(**self.language_data)

        self.assertEqual(language.profile_id, self.profile)
        self.assertEqual(language.name, "Spanish")
        self.assertEqual(language.proficiency, "N")

    def test_language_creation_with_invalid_proficiency(self):
        # Test creating a language with an invalid proficiency value
        language_data = {
            "profile_id": self.profile,
            "name": "Spanish",
            "proficiency": "X",
        }

        language = Language(**language_data)

        with self.assertRaises(ValidationError):
            language.full_clean()

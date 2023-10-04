from datetime import date
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from resume.models import (
    Profile,
    Language,
    EducationInformation,
    WorkExperience,
    ProfileDescription,
    ContactData,
    PersonalData,
)
from resume.serializers import (
    EducationInformationSerializer,
    WorkExperienceSerializer,
    ProfileSerializer,
)


class ViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.profile = Profile.objects.create(title="Title 1")

    def setUp(self):
        ProfileDescription.objects.all().delete()
        ContactData.objects.all().delete()
        EducationInformation.objects.all().delete()
        WorkExperience.objects.all().delete()

    def test_language_viewset(self):
        client = APIClient()
        # Create new language data: It should return HTTP_201_CREATED
        data = {"profile": self.profile.id, "name": "English", "proficiency": "F"}
        url = reverse("language-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "English")
        self.assertEqual(response.data["proficiency"], "F")

        # Get existing language data: It should return HTTP_200_OK
        language = Language.objects.get()
        get_url = reverse("language-detail", args=[language.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["name"], "English")

        # Update existing contact data: It should return HTTP_200_OK
        update_data = {
            "profile": self.profile.id,
            "name": "Spanish",
            "proficiency": "N",
        }
        update_url = reverse("language-detail", args=[language.id])
        update_response = client.put(update_url, update_data, format="json")

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Language.objects.get().name, "Spanish")
        self.assertEqual(Language.objects.get().proficiency, "N")

        # Delete language data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("language-detail", args=[language.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Language.objects.count(), 0)

        # TEST with incomplete data: It should return HTTP_400_BAD_REQUEST
        data = {"proficiency": "F"}
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("profile", response.data)

        # TEST with invalid data: It should return HTTP_400_BAD_REQUEST
        data = {"profile": self.profile.id, "name": "Spanish", "proficiency": "X"}
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("proficiency", response.data)

        # Get list of languages: Should return HTTP_200_OK
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_education_information_viewset(self):
        client = APIClient()
        # Create new education information data: It should return HTTP_201_CREATED
        data = {
            "profile": self.profile.id,
            "degree": "Master of Arts",
            "institution": "University B",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "description": "Description B",
        }
        url = reverse("educationinformation-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["degree"], "Master of Arts")
        self.assertEqual(response.data["institution"], "University B")

        # Get existing education information data: It should return HTTP_200_OK
        education_info = EducationInformation.objects.get()
        get_url = reverse("educationinformation-detail", args=[education_info.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        serializer = EducationInformationSerializer(education_info)
        self.assertEqual(get_response.data, serializer.data)
        self.assertEqual(get_response.data["degree"], "Master of Arts")
        self.assertEqual(get_response.data["institution"], "University B")

        # Update existing education information data: It should return HTTP_200_OK
        update_data = {
            "profile": self.profile.id,
            "degree": "Bachelor of Engineering",
            "institution": "University D",
            "start_date": "2022-01-01",
            "end_date": "2023-12-31",
            "description": "Description D",
        }
        update_url = reverse("educationinformation-detail", args=[education_info.id])
        update_response = client.put(update_url, update_data, format="json")

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            EducationInformation.objects.get().degree, "Bachelor of Engineering"
        )
        self.assertEqual(EducationInformation.objects.get().institution, "University D")

        # Delete education information data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("educationinformation-detail", args=[education_info.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationInformation.objects.count(), 0)

        # Test with incomplete data: It should return HTTP_400_BAD_REQUEST
        data = {
            "degree": "PhD",
            "institution": "University C",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
        }
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("profile", response.data)

        # Test with invalid data: It should return HTTP_400_BAD_REQUEST
        data = {
            "profile": "",  # Invalid
            "degree": "",
            "institution": "University E",
            "start_date": "2025-01-01",
            "end_date": "2024-12-31",
            "description": "Description E",
        }
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("profile", response.data)

        # Get list of education information: It should return HTTP_200_OK
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_work_experience_viewset(self):
        client = APIClient()
        # Create new work experience data: It should return HTTP_201_CREATED
        data = {
            "profile": self.profile.id,
            "company": "Company A",
            "company_description": "Description A",
            "position": "Position A",
            "start_date": "2022-01-01",
            "end_date": "2022-12-31",
            "description": "Description A",
            "skills": "Skill A",
        }
        url = reverse("workexperience-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["company"], "Company A")
        self.assertEqual(response.data["position"], "Position A")

        # Get existing work experience data: It should return HTTP_200_OK
        work_experience = WorkExperience.objects.get()
        get_url = reverse("workexperience-detail", args=[work_experience.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        serializer = WorkExperienceSerializer(work_experience)
        self.assertEqual(get_response.data, serializer.data)
        self.assertEqual(get_response.data["company"], "Company A")
        self.assertEqual(get_response.data["position"], "Position A")

        # Update existing work experience data: It should return HTTP_200_OK
        update_data = {
            "profile": self.profile.id,
            "company": "Company B",
            "company_description": "Description B",
            "position": "Position B",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "description": "Description B",
            "skills": "Skill B",
        }
        update_url = reverse("workexperience-detail", args=[work_experience.id])
        update_response = client.put(update_url, update_data, format="json")

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(WorkExperience.objects.get().company, "Company B")
        self.assertEqual(WorkExperience.objects.get().position, "Position B")

        # Delete work experience data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("workexperience-detail", args=[work_experience.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WorkExperience.objects.count(), 0)

        # Test with incomplete data: It should return HTTP_400_BAD_REQUEST
        data = {
            "company": "Company C",
            "position": "Position C",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "description": "Description C",
            "skills": "Skill C",
        }
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("profile", response.data)

        # Test with invalid data: It should return HTTP_400_BAD_REQUEST
        data = {
            "profile": "",  # Invalid
            "company": "",
            "company_description": "Description D",
            "position": "Position D",
            "start_date": "2025-01-01",
            "end_date": "2024-12-31",
            "description": "Description D",
            "skills": "Skill D",
        }
        response = client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("profile", response.data)

        # Get list of work experience: It should return HTTP_200_OK
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_profile_description_viewset(self):
        client = APIClient()
        # Create new profile description: It should return HTTP_201_CREATED
        data = {"profile": self.profile.id, "summary": "Test summary"}
        url = reverse("profiledescription-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProfileDescription.objects.count(), 1)
        self.assertEqual(ProfileDescription.objects.get().summary, "Test summary")

        # Get existing profile description: It should return HTTP_200_OK
        description = ProfileDescription.objects.get()
        get_url = reverse("profiledescription-detail", args=[description.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["summary"], "Test summary")

        # Update existing profile description: It should return HTTP_200_OK
        update_data = {"profile": self.profile.id, "summary": "Updated summary"}
        put_url = reverse("profiledescription-detail", args=[description.id])
        put_response = client.put(put_url, update_data, format="json")

        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProfileDescription.objects.get().summary, "Updated summary")

        # Delete contact profile description: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("profiledescription-detail", args=[description.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ProfileDescription.objects.count(), 0)

        # TEST with incomplete data: It should return HTTP_400_BAD_REQUEST
        invalid_data = {"summary": "Incomplete summary"}
        invalid_response = client.post(url, invalid_data, format="json")

        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)

        # TEST Get non-existent data: It should return HTTP_404_NOT_FOUND
        non_existent_url = reverse("profiledescription-detail", args=[999])
        non_existent_response = client.get(non_existent_url)

        self.assertEqual(non_existent_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_contact_data_viewset(self):
        client = APIClient()
        # Create new contact data: It should return HTTP_201_CREATED
        data = {
            "profile": self.profile.id,
            "phone_number": "123456789",
            "email": "nelson@example.com",
            "website": "https://example.com",
            "linkedin": "https://www.linkedin.com/in/desarrolladorpython",
            "github": "https://github.com/nelsonacos",
        }
        url = reverse("contactdata-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactData.objects.count(), 1)
        self.assertEqual(ContactData.objects.get().website, "https://example.com")

        # Get existing contact data: It should return HTTP_200_OK
        contact_data = ContactData.objects.get()
        get_url = reverse("contactdata-detail", args=[contact_data.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["website"], "https://example.com")

        # Update existing contact data: It should return HTTP_200_OK
        update_data = {
            "profile": self.profile.id,
            "phone_number": "987654321",
            "email": "nelson@example.com",
            "website": "https://updated.com",
            "linkedin": "https://www.linkedin.com/in/desarrolladorpython",
            "github": "https://github.com/nelsonacos",
        }
        put_url = reverse("contactdata-detail", args=[contact_data.id])
        put_response = client.put(put_url, update_data, format="json")

        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(ContactData.objects.get().website, "https://updated.com")

        # Delete contact personal data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("contactdata-detail", args=[contact_data.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ContactData.objects.count(), 0)

        # TEST with incomplete data: It should return HTTP_400_BAD_REQUEST
        invalid_data = {
            "phone_number": "123456789",
            "email": "invalidemail",  # Invalid email address
            "website": "https://example.com",
        }
        invalid_response = client.post(url, invalid_data, format="json")

        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)

        # TEST Get non-existent data: It should return HTTP_404_NOT_FOUND
        non_existent_url = reverse("contactdata-detail", args=[999])
        non_existent_response = client.get(non_existent_url)

        self.assertEqual(non_existent_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personal_data_viewset(self):
        client = APIClient()
        # Create new personal data: It should return HTTP_201_CREATED
        data = {
            "profile": self.profile.id,
            "first_name": "Nelson",
            "last_name": "Acosta",
            "date_of_birth": "1990-01-01",
            "address": "123 Main St",
        }

        url = reverse("personaldata-list")
        response = client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PersonalData.objects.count(), 1)
        self.assertEqual(PersonalData.objects.get().first_name, "Nelson")

        # Get existing personal data: It should return HTTP_200_OK
        personal_data = PersonalData.objects.get()
        get_url = reverse("personaldata-detail", args=[personal_data.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["first_name"], "Nelson")

        # Update existing personal data: It should return HTTP_200_OK
        update_data = {
            "profile": self.profile.id,
            "first_name": "Nelson",
            "last_name": "Acosta",
            "date_of_birth": "1995-01-01",
            "address": "456 Elm St",
        }
        put_url = reverse("personaldata-detail", args=[personal_data.id])
        put_response = client.put(put_url, update_data, format="json")

        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(PersonalData.objects.get().address, "456 Elm St")

        # Delete existing personal data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("personaldata-detail", args=[personal_data.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PersonalData.objects.count(), 0)

        # TEST with incomplete data: It should return HTTP_400_BAD_REQUEST
        invalid_data = {
            "first_name": "Nelson",
            "last_name": "Acosta",
            "date_of_birth": "1990-01-01",
        }
        invalid_response = client.post(url, invalid_data, format="json")

        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)

        # TEST Get non-existent data: It should return HTTP_404_NOT_FOUND
        non_existent_url = reverse("personaldata-detail", args=[999])
        non_existent_response = client.get(non_existent_url)

        self.assertEqual(non_existent_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_profile_viewset(self):
        client = APIClient()
        url = reverse("profile-list")
        # Get existing profile data: It should return HTTP_200_OK
        profile = Profile.objects.get()
        get_url = reverse("profile-detail", args=[self.profile.id])
        get_response = client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        serializer = ProfileSerializer(profile)
        self.assertEqual(get_response.data, serializer.data)

        # Update existing profile data: It should return HTTP_200_OK
        update_data = {"title": "Web Developer"}
        update_url = reverse("profile-detail", args=[self.profile.id])
        update_response = client.put(update_url, update_data, format="json")

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get().title, "Web Developer")

        # Delete profile data: It should return HTTP_204_NO_CONTENT
        delete_url = reverse("profile-detail", args=[self.profile.id])
        delete_response = client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)

        # Test with incomplete data: It should return HTTP_400_BAD_REQUEST
        incomplete_data = {}
        response = client.post(url, incomplete_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

        # Test with invalid data: It should return HTTP_400_BAD_REQUEST
        invalid_data = {"name": ""}
        response = client.post(url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

        # TEST Get non-existent data: It should return HTTP_404_NOT_FOUND
        non_existent_url = reverse("profile-detail", args=[999])
        non_existent_response = client.get(non_existent_url)

        self.assertEqual(non_existent_response.status_code, status.HTTP_404_NOT_FOUND)

        # Get list of profiles: It should return HTTP_200_OK
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsInstance(response.data, list)

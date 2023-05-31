from django.urls import include, path
from rest_framework import routers
from .views import LanguageViewSet, EducationInformationViewSet, WorkExperienceViewSet, ProfileDescriptionViewSet, ContactDataViewSet, PersonalDataViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'education-information', EducationInformationViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'profile-descriptions', ProfileDescriptionViewSet)
router.register(r'contact-data', ContactDataViewSet)
router.register(r'personal-data', PersonalDataViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import (
    LanguageViewSet,
    EducationInformationViewSet,
    WorkExperienceViewSet,
    AchievementViewSet,
    ProfileDescriptionViewSet,
    ContactDataViewSet,
    PersonalDataViewSet,
    ProfileViewSet,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"personal-data", PersonalDataViewSet)
router.register(r"contact-data", ContactDataViewSet)
router.register(r"profile-descriptions", ProfileDescriptionViewSet)
router.register(r"work-experiences", WorkExperienceViewSet)
router.register(r"achievements", AchievementViewSet)
router.register(r"education-information", EducationInformationViewSet)
router.register(r"languages", LanguageViewSet)


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Resume Creator Api")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

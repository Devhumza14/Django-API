from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewset, ProgramViewset

# This creates the automatic links
router = DefaultRouter()
router.register('students', StudentViewset, basename='student')
router.register('programs', ProgramViewset, basename='program')

urlpatterns = [
    path('', include(router.urls)),
]

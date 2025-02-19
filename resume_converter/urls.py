from django.urls import path
from .views import ResumeUploadView

urlpatterns = [
    path('', ResumeUploadView.as_view(), name='resume_upload'),
]
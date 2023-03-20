from django.urls import path
from . import views

urlpatterns = [
    path('upload_resume/', views.resume_upload, name='resume_upload'),
]

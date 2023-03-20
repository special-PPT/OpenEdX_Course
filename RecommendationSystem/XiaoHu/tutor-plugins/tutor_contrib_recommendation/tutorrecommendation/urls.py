from django.urls import path
from . import views

urlpatterns = [
    path("upload_resume", views.upload_resume, name="upload_resume"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('upload_resume/', views.ResumeFormView, name='form'),
]

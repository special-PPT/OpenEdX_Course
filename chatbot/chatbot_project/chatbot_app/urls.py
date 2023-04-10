from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('api/', views.chatbot_api, name='chatbot_api'),
]
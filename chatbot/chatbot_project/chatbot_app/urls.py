from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('chatbot/api/', views.chatbot_api, name='chatbot_api'),
    path('crawl/', views.crawl_text, name='crawl_text'),
]
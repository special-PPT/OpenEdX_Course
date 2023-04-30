from rest_framework import serializers
from .models import Resume, Courses

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume 
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
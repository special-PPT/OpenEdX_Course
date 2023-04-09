from django.db import models


class Resume(models.Model):
    user_name = models.CharField(max_length=255)
    resume_file = models.FileField(upload_to='resumes/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
class Courses(models.Model):
    course_name = models.CharField(max_length=3000)
    category = models.CharField(max_length=30)
    difficuly_rating = models.CharField(max_length=30)
    course_url = models.CharField(max_length=3000)
    course_description = models.TextField(max_length=5000)

    def __str__(self):
        return self.course_name

    

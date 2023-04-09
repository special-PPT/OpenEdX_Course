from django.http import HttpResponse

def upload_resume(request):
    return HttpResponse("<h1>Upload your resume</h1>")

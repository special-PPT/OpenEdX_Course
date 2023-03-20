from django.shortcuts import render
from .forms import ResumeUploadForm
from .models import Resume


def resume_upload(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("File uploaded successfully.")
            return render(request, 'success.html')
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = ResumeUploadForm()
    return render(request, 'resume_upload.html', {'form': form})

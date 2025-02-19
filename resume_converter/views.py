# Create your views here.
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django import forms
from pdfminer.high_level import extract_text

# Form
class ResumeUploadForm(forms.Form):
    resume = forms.FileField()

# View
class ResumeUploadView(View):
    def get(self, request):
        form = ResumeUploadForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request):
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES['resume']
            fs = FileSystemStorage()
            filename = fs.save(resume_file.name, resume_file)
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

            # Extract text from PDF
            extracted_text = extract_text(file_path)
            html_content = f"<html><body><pre>{extracted_text}</pre></body></html>"

            return HttpResponse(html_content)
        return render(request, 'upload.html', {'form': form})

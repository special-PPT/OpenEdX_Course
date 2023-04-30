from django.shortcuts import render
from .forms import ResumeUploadForm
from .models import Resume, Courses
from .serializer import ResumeSerializer, CourseSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
import pickle
import numpy
import pandas
import docx2txt
import nltk
from pathlib import Path
import pkg_resources

class ResumeView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

def convert_to_text(file):
    try:
        txt = docx2txt.process(file)
        if txt:
            text = txt.replace('\t', ' ')
            return text
        return None
    except FileNotFoundError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
def extract_text(input_text):
    skill_list = ['machine learning',
    'cooking',
    'painting',
    'deep learning',
    'python',
    'film making',
    'cinematography',
    'dash',
    'java',
    'web application',
    'agile',
    'developed',
    'integrated',
    'handled',
    'designed',
    'tested']
    nltk.download('stopwords')
    nltk.download('punkt')

    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    stop_filtered = [w for w in word_tokens if w not in stop_words]

    filtered_tokens = [w for w in stop_filtered if w.isalpha()]

    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    skills = set()

    #single words
    for token in filtered_tokens:
        if token.lower() in skill_list:
            skills.add(token)
    
    #hyphenated words
    for ngram in bigrams_trigrams:
        if ngram.lower() in skill_list:
            skills.add(ngram)

    if len(skills) > 0:
      return True
 
    return False

def get_suggestions(resume):
    text = convert_to_text(resume)
    list_text = text.split("\n")
    content = []
    for t in list_text:
        skills = extract_text(t)
        if skills:
            content.append(t)
    return content

def prediction(skills):
    try:

        # current_dir = Path(__file__).resolve().parent
        # transformer_path = current_dir / "resources" / "transformer.sav"
        # rec_model_path = current_dir / "resources" / "rec_model.sav"
        transformer_path = pkg_resources.resource_filename('course_recommendation', 'resources/transformer.sav')
        rec_model_path = pkg_resources.resource_filename('course_recommendation', 'resources/rec_model.sav')

        with open(transformer_path, "rb") as transformer_file:
            transformer = pickle.load(transformer_file)

        with open(rec_model_path, "rb") as rec_model_file:
            rec_model = pickle.load(rec_model_file)

        pred = []
        for skill in skills:
            X = transformer.transform([skill])
            y_pred = rec_model.predict(X)
            pred.append(y_pred[0])
        return list(set(pred))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def ResumeFormView(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            resume = form.cleaned_data['resume_file']
            content = get_suggestions(resume)
            result = prediction(content)
            courses = Courses.objects.filter(category = result[0]).values()[:5]
            serialized_item = CourseSerializer(courses, many=True)
            return render(request, 'course_recommendation/prediction.html', {"data":serialized_item.data})
    
    form = ResumeUploadForm()
    return render(request, 'course_recommendation/resume_upload.html', {"form":form})


from django.shortcuts import render
from .forms import ResumeUploadForm
from .models import Resume
from .serializer import ResumeSerializer
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
        # transformer = pickle.load(open("C:\\Users\\Kavya Venkatesh\\Capstone project\\OpenEdX_Course-main\\RecommendationSystem\\XiaoHu\\BoeingRecommendation\\course_recommendation\\transformer.sav", "rb"))
        # rec_model = pickle.load(open("C:\\Users\\Kavya Venkatesh\\Capstone project\\OpenEdX_Course-main\\RecommendationSystem\\XiaoHu\\BoeingRecommendation\\course_recommendation\\rec_model.sav", "rb"))

        transformer = pickle.load(open(
            "/Users/corallee/Downloads/Capstone project/OpenEdX_Course-main/RecommendationSystem/XiaoHu/BoeingRecommendation/course_recommendation/transformer.sav",
            "rb"))
        rec_model = pickle.load(open(
            "/Users/corallee/Downloads/Capstone project/OpenEdX_Course-main/RecommendationSystem/XiaoHu/BoeingRecommendation/course_recommendation/rec_model.sav",
            "rb"))

        pred = []
        for skill in skills:
            X = transformer.transform([skill])
            y_pred = rec_model.predict(X)
            pred.append(y_pred)
        return pred
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
            return render(request, 'prediction.html', {"data":result})
        
    form = ResumeUploadForm()
    return render(request, 'resume_upload.html', {"form":form})


# def resume_upload(request):
#     if request.method == 'POST':
#         form = ResumeUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print("File uploaded successfully.")
#             return render(request, 'success.html')
#         else:
#             print("Form is not valid.")
#             print(form.errors)
#     else:
#         form = ResumeUploadForm()
#     return render(request, 'resume_upload.html', {'form': form})


# class StudentView(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# def status(df):
#     try:
#         transformer = pickle.load(open("C:\\Users\\Kavya Venkatesh\\Capstone project\\OpenEdX_Course-main\\RecommendationSystem\\XiaoHu\\BoeingRecommendation\\course_recommendation\\transformer.sav", "rb"))
#         rec_model = pickle.load(open("C:\\Users\\Kavya Venkatesh\\Capstone project\\OpenEdX_Course-main\\RecommendationSystem\\XiaoHu\\BoeingRecommendation\\course_recommendation\\rec_model.sav", "rb"))
#         X = transformer.transform([df])
#         y_pred = rec_model.predict(X)
#         return y_pred
#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    

# def FormView(request):
#     if request.method == "POST":
#         form = StudentDetailsForm(request.POST or None)

#         if form.is_valid():
#             text = form.cleaned_data['text']
#             result = status(text)
#             return render(request, 'suggestion.html', {"data":result})
        
#     form = StudentDetailsForm()
#     return render(request, 'form.html', {'form':form})

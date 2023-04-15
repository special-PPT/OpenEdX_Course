from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .gpt_api import chat_gpt

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('input', '')
        response = chat_gpt(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'})

# Create your views here.
def chatbot(request):
    return render(request, 'chatbot.html')
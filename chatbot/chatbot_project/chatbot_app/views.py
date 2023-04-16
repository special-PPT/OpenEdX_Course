from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .gpt_api import chat_gpt
from .web_crawler import get_page_text

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('input', '')
        response = chat_gpt(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'})

# Create your views here.
def chatbot_view(request):
    return render(request, 'chatbot.html')

def crawl_text(request):
    url = 'https://www.coursera.org/learn/learn-to-program'
    try:
        page_text = get_page_text(url)
        # You can save the fetched text to the database, send it to a template, or process it further here
    except Exception as e:
        # Handle the exception if the web page cannot be fetched
        print(e)

    # Render a template with the fetched text
    context = {'page_text': page_text}
    return render(request, 'course.html', context)

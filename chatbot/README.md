This is a docker-based course chatbot for Boeing customized Open edX. Users can ask about a course.
The chatbot uses Open GPT as the platform to support the conversation.

To connect to the Open edX
1. Replace your api-key inside Chatbot/chatbot_project/chatbot_app/gpt_api.py
`openai.api_key = "sk-Your Key"`
2. Replace the course content url inside the same file
`course_url = 'a course website url'`

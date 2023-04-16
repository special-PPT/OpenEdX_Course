import openai
from .web_crawler import get_page_text

openai.api_key = "sk-your key"
messages = []

# get course content through web crawler
course_url = 'https://www.coursera.org/learn/learn-to-program'
course_info = get_page_text(course_url)

# make respond have more emoji
wave_hand = "\U0001F44B"
smile_face = "\U0001F60A"
end_message = f"{wave_hand} {smile_face}"

# initial course content
def insert_start_course_info():
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    messages.append({"role": "system", "content": course_info})

insert_start_course_info()


def chat_gpt(user_input):
    global messages  # add this line to access the global variable

    # empty course content
    if user_input.lower() == "quit":
        messages = []
        insert_start_course_info()
        return "Bye, Have a Good Day!" + end_message

    user_input = user_input + "write a helpful message and use emoji in your response"
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        # max_tokens=128,
        top_p=0.5,
    )

    messages.append({"role": "system", "content": response.choices[0]["message"]["content"]})

    return response.choices[0]["message"]["content"]

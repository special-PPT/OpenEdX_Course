import openai
import sys
import os

openai.api_key = "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"
messages = []
course_info = "Here I give you the information of a particular class. " \
              "Please answer my following question based on this information." \
              "Class name: UH2855 (Calhoun Transdisciplinary Fusion Studio 1) " \
              "Studio Class Location: Honors College Studios (Squires Student Center) " \
              "Lab Locations: Discovery Studio (Hillcrest Hall); Future Manufacturing Lab (Kelly Hall Rm 130); Honors " \
              "College Studios (Squires 134)" \
              "Class time: Fridays, 1:25—4:15pm" \
              "Class type: In-person Instruction"



def insert_start_course_info():
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    messages.append({"role": "system", "content": course_info})
    messages.append({"role": "system",
                     "content": "do not mention pandemic, and concise, "
                                "please note that instructor may update the course information"})


insert_start_course_info();


def chat_gpt(user_input):
    global messages  # add this line to access the global variable

    if user_input.lower() == "quit":
        messages = []
        insert_start_course_info()
        return "Bye, Have a Good Day!"

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

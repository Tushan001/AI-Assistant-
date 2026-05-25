import os
from config import apikey
from groq import Groq
import time
from voice import say


chatStr = ""
# For chat purpose
def chat(query):
    client = Groq(
    api_key=apikey
)
    global chatStr

    chatStr += f"Tushan: {query}\n AXIOM: "

    text = f"OpenAI response for prompt: {query} \n******************\n\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=60,
        messages=[
    {
        "role": "system",
        "content": "You are AXIOM, a concise futuristic AI assistant. Keep responses short and direct."
    },
    {
        "role": "user",
        "content": query
    }
]
    )
    say(response.choices[0].message.content)
    time.sleep(1)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content

# AI part
def ai(prompt):
    client = Groq(api_key=apikey)
    text = f"OpenAI response for prompt: {prompt} \n******************\n\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(response.choices[0].message.content)
    text += response.choices[0].message.content
# File saving part

    os.makedirs("OpenAI", exist_ok=True)

    filename = ''.join(prompt.split('intelligence')[1:]).strip()
    if not filename:
        filename = "response"
    safe_filename = "".join(
        c for c in filename if c.isalnum() or c in (" ", "_", "-")
        ).strip()
    if not safe_filename:
        safe_filename = "response"

    with open(os.path.join("OpenAI", f"{safe_filename}.txt"), "w", encoding="utf-8") as f:
        f.write(text)
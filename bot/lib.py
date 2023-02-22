import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0.6,
        stop=["You:", "AI:"]
    )
    return response['choices'][0]['text']

def get_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        # model=MODEL_ENGINE,
        n=1,
        size="1024x1024"
    )
    img_url = response['data'][0]['url']
    return img_url


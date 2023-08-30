import json
import openai
import os
from exceptions import BadOpenAIResponse

DEFAULT_SONG_THEME = "something random"
LINES_OF_LYRICS = 4
MAX_WORDS_PER_LINE = 8

def make_openai_api_request(content):
    openai.organization = os.getenv("OPENAI_ORG")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chatgpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": content}]
    )

    return chatgpt_response

def song_response_parser(chatgpt_response):
    if len(chatgpt_response.choices) == 0:
        raise BadOpenAIResponse

    resp = {}

    json_object = json.loads(chatgpt_response.choices[0].message.content)
    resp["song_title"] = json_object.get("song_title")
    resp["song_lyrics"] = json_object.get("song_lyrics")

    return resp

def get_song_template(song_theme=DEFAULT_SONG_THEME, lines_of_lyrics=LINES_OF_LYRICS):
    return f"Write me a song name and ${lines_of_lyrics} lines of lyrics for a song about ${song_theme}. Each line in the lyrics should have a maximum of ${MAX_WORDS_PER_LINE} words. I want the response in a JSON format where the song title has the key 'song_title' and the lyrics have the key 'song_lyrics'"

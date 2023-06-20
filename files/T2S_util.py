""" import requests

url = "https://api.elevenlabs.io/v1/models"

headers = {
  "Accept": "application/json",
  "xi-api-key": "<22b28efb7258a43bb2192741fac7af1f>"
}

response = requests.get(url, headers=headers)

print(response.text)
 """
""" 
import os
from subprocess import call
from pydub import AudioSegment
from elevenlabs import clone, generate, play, set_api_key

def play(text, voice):
    set_api_key("22b28efb7258a43bb2192741fac7af1f")
    audio = generate(
        text=text,
        voice=voice,
        model="eleven_monolingual_v1"
    )
    play(audio)

 """
""" def get_flac_list(target_dir):
    flac_list = []
    for file in os.listdir(target_dir):
        if file.endswith(".flac"):
            return_data = f"{target_dir}/{file}"
            flac_list.append(return_data)
    return flac_list

def clone_voice(name, description, target_dir):
    flac_list = get_flac_list(target_dir)
    Voice = clone(name, description, flac_list)
    return Voice
#main function
def main():
    print('Dont panic!')
    set_api_key("22b28efb7258a43bb2192741fac7af1f")
    #target_dir = sys.argv[1]
    target_dir = "./sounds"
    flac_list = get_flac_list(target_dir)
    voice = clone(
        name="Alex",
        description="An old American male voice with a slight hoarseness in his throat. Perfect for news",
        files = flac_list,
    )
    audio = generate(text="Hi! I'm a cloned voice!", voice=voice)
    play(audio)
    print('So long and thanks for all the fish!') """

from elevenlabs import generate, play, set_api_key

def play_text(text):
    set_api_key("22b28efb7258a43bb2192741fac7af1f")
    audio = generate(
        text=text,
        voice="Arnold",
        model="eleven_monolingual_v1"
    )
    play(audio)
    # audio = generate(
    #     text=text,
    #     voice="Adam",
    #     model="eleven_monolingual_v1"
    # )
    # play(audio)
    # audio = generate(
    #     text=text,
    #     voice="Antoni",
    #     model="eleven_monolingual_v1"
    # )
    # play(audio)





from elevenlabs import generate, play, set_api_key

def play_text(text):
    set_api_key("22b28efb7258a43bb2192741fac7af1f")
    audio = generate(
        text=text,
        voice="Arnold",
        model="eleven_monolingual_v1"
    )
    play(audio)

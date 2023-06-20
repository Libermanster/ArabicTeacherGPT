from elevenlabs import generate, play

audio = generate(
  text="my name is bella nice to meet you",
  voice="Arnold",
  model="eleven_monolingual_v1"
)

play(audio)

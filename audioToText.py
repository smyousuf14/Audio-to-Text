import speech_recognition as sr
from os import path
from pydub import AudioSegment

#convert the mp3 file into wav file.
sound = AudioSegment.from_mp3("audio.mp3")
sound.export("audio.wav", format = "wav")

#transcribe the audio file
AUDIO_FILE = "audio.wav"

#use the audio file as the audio source
r = sr.Recgonizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source) #read the entire audio file.
	
	print(r.recognize_google(audio))
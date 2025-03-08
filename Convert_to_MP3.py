from pydub import AudioSegment

audio = AudioSegment.from_wav("./audios/test2.wav")

#convert wav to mp3
audio = audio.fade_in(2000)
audio.export("./audios/test2.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("./audios/test2.mp3")
print("done")
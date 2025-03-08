# audio file formats (.mp3, .wav, .flac)

import wave

obj = wave.open("./audios/test2.wav", "rb")

print("number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("number of frames", obj.getnframes())
print("Parameters", obj.getparams())

TimeAudio = obj.getnframes() / obj.getframerate()

print("total audio time ", TimeAudio,"s")

frames = obj.readframes(-1)
print("frames", type(frames), type(frames[0]))
print("length of frames", len(frames) / 4)

obj.close()

#create an new audio

obj_new = wave.open("./audios/test2_new.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)

obj_new.close()
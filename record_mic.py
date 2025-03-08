import pyaudio
import wave

Frames_per_buffer = 3200
Format = pyaudio.paInt16
Channels = 1 
Rate = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=Format,
    channels=Channels,
    rate=Rate,
    input=True,
    frames_per_buffer=Frames_per_buffer
)

print("start recording")

seconds = 5
frames = []

for i in range(0, int(Rate/Frames_per_buffer*seconds)):
    data = stream.read(Frames_per_buffer)
    frames.append(data)
    

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("./audios/Output.wav", "wb")
obj.setnchannels(Channels)
obj.setsampwidth(p.get_sample_size(Format))
obj.setframerate(Rate)
obj.writeframes(b"".join(frames))

obj.close()

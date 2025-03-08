import numpy as np
import wave
import matplotlib.pyplot as plt


obj = wave.open("./audios/test2.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels() 
signal_wave = obj.readframes(-1)


obj.close()

t_audio = n_samples / sample_freq

print(t_audio)

#create plot

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

if n_channels == 2:
    signal_array = signal_array.reshape(-1, n_channels)
    signal_array = signal_array[:, 0]  # Take the left channel

times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
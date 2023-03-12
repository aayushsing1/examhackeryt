import sounddevice as sd
import soundfile as sf

sample_rate = 44100
duration = 5 #in seconds
channels = 2 

#start recording

print('Recording Audio: ')
recording = sd.rec(int(sample_rate*duration),samplerate=sample_rate, channels=channels)

#wait for recording to finish

sd.wait()

#save recorded file
file_name = input('Enter File Name:: ')
sf.write(file_name+'.wav', recording, sample_rate)

print(f'Audio saved as {file_name}.wav')

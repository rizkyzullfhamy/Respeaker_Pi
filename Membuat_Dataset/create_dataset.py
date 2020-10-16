import pyaudio
import wave
import time
import os.path
save_path = '/home/pi/Documents/BISMILLAH TA/SENSOR/Membuat_Dataset/Hasil_Audio'
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 4
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 0  # refer to input device id
CHUNK = 1024
RECORD_SECONDS = 5
iter = 0
def Respeaker_Access(iter):
    p = pyaudio.PyAudio()
    stream = p.open(
        rate=RESPEAKER_RATE,
        format=p.get_format_from_width(RESPEAKER_WIDTH),
        channels=RESPEAKER_CHANNELS,
        input=True,
        input_device_index=RESPEAKER_INDEX,
    )
    print('Record\n')
    frames = []
    for i in range(0,int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        
    print('Done Recording\n')
    nama_file = ('DataRec_' + str(iter) + '.wav')
    completeName = os.path.join(save_path, nama_file)
    print('SAVED : ' + nama_file) 
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(completeName,'w')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":

    while(True):
        iter += 1
        print(iter)
        Respeaker_Access(iter)
        if (iter == 5):
            break




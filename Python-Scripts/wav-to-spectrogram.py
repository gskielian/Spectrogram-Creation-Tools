#!/usr/bin/env python

import os
import wave
import matplotlib
matplotlib.use('Agg')
import pylab
import sys

def create_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_data(wav_file)
    pylab.figure(num=None, figsize=(20, 10))
    pylab.axis('off')
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('spectrogram_-_%s' % os.path.splitext(wav_file)[0],bbox_inches='tight', pad_inches = 0)


def get_wav_data(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

if __name__ == '__main__':
    wav_file = sys.argv[1]
    create_spectrogram(wav_file)

from numpy import ndarray
from typing import List
import soundfile as sf
from scipy.io import wavfile
import scipy.signal as ss
import numpy as np

fragment = ndarray
fragmented_list = list[fragment]()
track = ndarray

##############
# Constantes #
##############
path = "..\\..\\resources\\wav_files\\Arctic Monkeys - Do I Wanna Know.wav"
filename = "Test.wav"
ovrlp = 0
N = 8192
fs = 44000



class TrackManager(object):
    def __init__(self):
        print("TrackManager created")
        self.trck = track([0])
        self.fragmented_list = fragmented_list
        self.new_track = [[0,0]]

    def set_track(self, trck: track):
        print("TrackManager: set_track")
        self.trck = trck

    def get_track(self) -> track:
        print("TrackManager: get_track")
        return self.trck

    def open_sound_file(self, path: str):
        print("TrackManager: open_sound_file")
        samplerate, data = wavfile.read(path,mmap=False)
        self.set_track(data)

    def save_sound_file(self, filename: str):
        print("TrackManager: save_sound_file")
        wavfile.write(filename, fs, self.new_track)

    def chunks(self, N, ovrlp):
        for i in range(0, len(self.trck), N-ovrlp):
            self.fragmented_list.append(self.trck[i:i+N])
        for i in range(0, len(self.fragmented_list)):
            self.fragmented_list[i] = np.pad(self.fragmented_list[i],(0,N-len(self.fragmented_list[i])))

    def fragment_list(self):
        self.chunks(N,ovrlp)
        # for i in range(0, len(self.fragmented_list)):
        #     self.fragmented_list[i] = Window.blackman(self.fragmented_list[i])

    def get_fragmented_list(self) -> fragment_list:
        print("TrackManager: get_fragmented_list")
        return self.fragmented_list

    def set_fragment_list_and_assemble(self, fragmented_list):
        print("TrackManager: set_fragment_list_and_assemble")
        print(len(self.fragmented_list))
        for i in range(0, len(self.fragmented_list)-1):
            print(self.new_track)
            print(i)
            print(self.fragmented_list[i])
            self.new_track = np.concatenate((self.new_track, self.fragmented_list[i]))



class Window(object):
    def __init__(self):
        print("Window choosed")

    def blackman(a: ndarray) -> ndarray:
        return np.multiply(a, np.blackman(len(a)))

    def bartlett(a: ndarray) -> ndarray:
        return np.multiply(a, np.bartlett(len(a)))

    def hamming(a: ndarray) -> ndarray:
        return np.multiply(a, np.hamming(len(a)))

    def blackmanharris(a: ndarray) -> ndarray:
        return np.multiply(a, ss.blackmanharris(len(a)))


if __name__ == '__main__':
    A = TrackManager()
    ar = np.array([1,2,3,4,5,6,7,8,9,10])
    # A.set_track(ar)
    A.open_sound_file(path)
    A.fragment_list()
    B = A.get_fragmented_list()
    A.set_fragment_list_and_assemble(B)
    A.save_sound_file(filename)
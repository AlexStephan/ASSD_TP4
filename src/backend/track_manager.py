from numpy import ndarray
from typing import List
import soundfile as sf
from scipy.io import wavfile
import scipy.signal as ss
import numpy as np

fragment = ndarray
fragment_list = list[fragment]()
track = ndarray

##############
# Constantes #
##############
ovrlp = 1
N = 3



class TrackManager(object):
    def __init__(self):
        print("TrackManager created")
        self.trck = track([0])
        self.fragment_list = fragment_list

    def set_track(self, trck: track):
        print("TrackManager: set_track")
        self.trck = trck

    def get_track(self) -> track:
        print("TrackManager: get_track")
        return self.trck

    def open_sound_file(self, path: str):
        print("TrackManager: open_sound_file")
        samplerate, data = wavfile.read(path)
        self.set_track(data)

    def save_sound_file(self, path: str):
        print("TrackManager: save_sound_file")

    def chunks(self, N, ovrlp):
        for i in range(0, len(self.trck), N-ovrlp):
            self.fragment_list.append(self.trck[i:i+N].copy())
        for i in range(0, len(self.fragment_list)):
            self.fragment_list[i].resize(N)

    def get_fragment_list(self) -> fragment_list:
        print("TrackManager: get_fragment_list")
        self.chunks(N,ovrlp)
        print(self.fragment_list)
        for i in range(0, len(self.fragment_list)):
            self.fragment_list[i] = Window.blackman(self.fragment_list[i])
        return self.fragment_list

    def set_fragent_list_and_assemble(self, fragment_list):
        print("TrackManager: set_fragent_list_and_assemble")


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
    A.set_track(ar)
    A.get_fragment_list()
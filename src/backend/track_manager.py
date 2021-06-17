from numpy import ndarray
from typing import List
import soundfile as sf
from scipy.io import wavfile

fragment = ndarray
fragment_list = List[fragment]
track = ndarray

#
# Constantes
#



class TrackManager(object):
    def __init__(self):
        print("TrackManager created")
        self.trck = track([0])

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

    def get_fragment_list(self) -> fragment_list:
        print("TrackManager: get_fragment_list")
        return []

    def set_fragent_list_and_assemble(self, fragment_list):
        print("TrackManager: set_fragent_list_and_assemble")

if __name__ == '__main__':
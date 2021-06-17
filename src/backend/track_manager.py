from numpy import ndarray


class TrackManager(object):
    def __init__(self):
        print("TrackManager created")
        self.track = ndarray([0])

    def set_track(self, track: ndarray):
        print("TrackManager: set_track")
        self.track = track

    def get_track(self) -> ndarray:
        print("TrackManager: get_track")
        return ndarray([0])

    def open_sound_file(self, path: str):
        print("TrackManager: open_sound_file")
        self.set_track(ndarray([0]))

    def save_sound_file(self, path: str):
        print("TrackManager: save_sound_file")

from numpy import ndarray

from src.backend.track_manager import fragment,fragment_list,track

class ARMAPoint(object):
    def __init__(self):
        print("ARMAPoint created")

    def set_fragment_and_calculate_arma(self, fragm : fragment):
        print("ARMAPoint set")

    def get_fundamental_frequency(self) -> float:
        print("ARMAPoint get_fundamental_frequency")
        return 0

    def synthesize_from_fundamental_frequency(self, fundamental: float):
        print("ARMAPoint synthesize")

    def get_synthesized_fragment(self) -> fragment:
        print("ARMAPoint get synthesize fragment")
        return fragment([0])

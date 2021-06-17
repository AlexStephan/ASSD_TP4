from numpy import ndarray

class ARMAPoint(object):
    def __init__(self):
        print("ARMAPoint created")

    def set_fragment_and_calculate_arma(self, fragment):
        print("ARMAPoint set")

    def get_fundamental_frequency(self) -> float:
        print("ARMAPoint get_fundamental_frequency")
        return 0

    def synthesize_from_fundamental_frequency(self, fundamental: float):
        print("ARMAPoint synthesize")

    def get_synthesized_fragment(self) -> ndarray:
        print("ARMAPoint get synthesize fragment")
        return ndarray([0])

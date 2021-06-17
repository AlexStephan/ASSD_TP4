from numpy import ndarray

from src.backend.track_manager import fragment,fragment_list,track

class ARMAPoint(object):
    def __init__(self):
        print("ARMAPoint created")
        self.position = ndarray([0])
        self.arma_data = ndarray([]) #lo mas probable es q sean lo coeficientes

    def set_fragment_and_calculate_arma(self, fragm : fragment):
        print("ARMAPoint set")
        #tambien actualizar position, con los coeficientes de escalamiento adecuados
        #calcular fundamental frequency si se puede

    def get_fundamental_frequency(self) -> float:
        print("ARMAPoint get_fundamental_frequency")
        return 0

    def synthesize_from_fundamental_frequency(self, fundamental: float):
        print("ARMAPoint synthesize")

    def get_synthesized_fragment(self) -> fragment:
        print("ARMAPoint get synthesize fragment")
        return fragment([0])

    def get_position(self) -> ndarray:
        return self.position

    def get_arma_data(self) -> ndarray:
        return self.arma_data

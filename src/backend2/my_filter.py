from typing import List
from numpy import ndarray
import numpy as np
import scipy.signal as ss

coeff = List


class MyFilter(object):
    def __init__(self, coefficients: coeff = None):
        #print("MyFilter created")
        self.coefficients = None
        self.zeros = None
        self.poles = None  # La estrella del show
        self.gain = None
        self.degree = None
        self.angles = None
        self.set_coefficients(coefficients)

    def set_coefficients(self, coefficients: coeff):
        self.coefficients = coefficients
        if self.coefficients is not None:
            self.degree = len(self.coefficients)
            denominator = [1]
            denominator.extend(np.multiply(coefficients, -1))
            self.zeros,self.poles,self.gain = ss.tf2zpk([1],denominator)

            self.angles = []
            for p in self.poles:
                self.angles.append(np.abs(np.angle(p)))
            self.angles.sort()

    def get_coefficients(self) -> coeff:
        return self.coefficients

    def get_angles(self) -> List:
        return self.angles

    def get_zeros(self) -> List:
        return self.zeros

    def get_poles(self) -> List:
        return self.poles

from src.backend.arma_point import ARMAPoint
from typing import List
from scipy import spatial


#en esta version, se asume que "position" es un arreglo con todos los picos del espectro, con o sin ruido

class ARMASpace(object):
    def __init__(self):
        print("ARMASpace craeated")
        self.pointList = []

    def erase_all_points(self):
        print("ARMASpace: all points removed")
        self.pointList = []

    def add_point(self, point: ARMAPoint):
        print("ARMASpace: point added")
        self.pointList.append(point)

    def add_points(self, list_of_points: List):
        for p in list_of_points:
            self.add_point(p)

    def get_closest_point(self, point: ARMAPoint) -> ARMAPoint:
        print("ARMASpace: returned closest point")
        if self.pointList != []:
            #WIP
            print("WIP")
        else:
            return ARMAPoint()
    # todo: agregarle interpolación para puntos intermedios

from src.backend.arma_point import ARMAPoint
from typing import List
from scipy import spatial
#A=[[1,1],[0,1],[1,0]]
#tree = spatial.KDTree(A)
#tree.query([0,0])


class ARMASpace(object):
    def __init__(self):
        print("ARMASpace created")
        self.pointList = []
        self.tree = None

    def erase_all_points(self):
        print("ARMASpace: all points removed")
        self.pointList = []
        self.tree = None

    def add_point(self, point: ARMAPoint):
        print("ARMASpace: point added")
        self.pointList.append(point)

    def add_points(self, list_of_points: List):
        for p in list_of_points:
            self.add_point(p)

    def create_tree_with_added_points(self):
        if self.pointList == []:
            self.tree = None
        else:
            positions = []
            for p in self.pointList:
                positions.append(p.get_position())
            self.tree = spatial.KDTree(positions)

    def get_closest_point(self, point: ARMAPoint) -> ARMAPoint:
        print("ARMASpace: returned closest point")
        if self.tree != None:
            return self.pointList[self.tree.query(point.get_position())[1]]
        else:
            return ARMAPoint()
    # todo: agregarle interpolación para puntos intermedios

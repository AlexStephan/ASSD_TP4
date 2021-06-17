from src.backend.arma_point import ARMAPoint

class ARMASpace(object):
    def __init__(self):
        print("ARMASpace created")

    def erase_all_points(self):
        print("ARMASpace: all points removed")

    def add_point(self, point: ARMAPoint):
        print("ARMASpace: point added")

    def get_closest_point(self, point: ARMAPoint) -> ARMAPoint:
        print("ARMASpace: returned closest point")
        return ARMAPoint()

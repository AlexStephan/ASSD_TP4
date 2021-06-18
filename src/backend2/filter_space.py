from src.backend2.my_filter import MyFilter
from typing import List
from scipy import spatial
import numpy as np

class FilterSpace(object):
    def __init__(self):
        print("FilterSpace created")
        self.filter_list = []
        self.tree = None

    def erase_all_filters(self):
        self.filter_list = []
        self.tree = None

    def add_filter(self, filter: MyFilter):
        self.filter_list.append(filter)

    def add_filters(self, filters: List):
        for f in filters:
            self.add_filter(f)

    def create_tree_from_filters(self):
        if self.filter_list == []:
            self.tree = None
        else:
            positions = []
            for f in self.filter_list:
                positions.append(self.__apply_position_weight(f.get_angles()))
            self.tree = spatial.KDTree(positions)

    def get_closest_filter_index(self, filt: MyFilter) -> int:
        if self.tree is not None:
            return self.tree.query(filt.get_angles())[1]
        else:
            return -1

    def get_filter(self, index: int) -> MyFilter:
        if self.tree is not None:
            return self.filter_list[index]
        else:
            return MyFilter()

    def __apply_position_weight(self, angles: List) -> List:
        weighted = []
        for i,a in enumerate(angles):
            weighted.append(a*self.__weight(i))
        return weighted

    def __weight(self, i: int) -> float:
        return np.power(0.6, i)

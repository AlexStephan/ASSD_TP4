from src.backend2.my_filter import MyFilter
from typing import List
from scipy import spatial
import numpy as np
from enum import Enum


class Mode(Enum):
    Angles = 1
    Poles = 2


def separate(v: List)->List:
    rta = []
    for i in v:
        rta.extend([np.real(i),np.imag(i)])
    return rta


class FilterSpace(object):
    def __init__(self):
        print("FilterSpace created")
        self.filter_list = []
        self.tree = None
        self.mode = Mode.Poles

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
            if self.mode == Mode.Poles:
                positions = []
                for f in self.filter_list:
                    positions.append(separate(f.get_poles()))
                self.tree = spatial.KDTree(positions)
            elif self.mode == Mode.Angles:
                positions = []

    def get_closest_filter_index(self, filt: MyFilter) -> int:
        if self.tree is not None:
            if self.mode == Mode.Poles:
                return self.tree.query(separate(filt.get_poles()))[1]
        else:
            return -1

    def get_filter(self, index: int) -> MyFilter:
        if self.tree is not None:
            return self.filter_list[index]
        else:
            return MyFilter()

    def get_closest_filter(self, filt: MyFilter) -> MyFilter:
        if self.tree is not None:
            return self.get_filter(self.get_closest_filter_index(filt))
        else:
            return MyFilter()


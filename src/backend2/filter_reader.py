from typing import List


class FilterReader(object):
    def __init__(self):
        print("FilterReader created")
        self.filter_collection = []

    def open_file(self, path:str) -> bool:
        print("FilterReader open_file")
        return True

    def get_filters(self) -> List:
        print("FilterReader get_filters")
        return self.filter_collection

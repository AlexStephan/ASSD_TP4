from typing import List
import csv
import numpy as np

class FilterWriter(object):
    def __init__(self):
        print("FilterWriter created")
        #self.filter_collection = []

    def save_file(self, path: str, filters: List) -> bool:
        return True

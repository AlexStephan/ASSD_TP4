from typing import List
import csv
import numpy as np

class FilterReader(object):
    def __init__(self):
        print("FilterReader created")
        self.filter_collection = []

    def open_file(self, path:str) -> bool:
        print("FilterReader open_file")
        a = True
        try:
            with open(path) as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                for row in data:
                    self.filter_collection.append(row)
                self.filter_collection = np.array(self.filter_collection,float)
                self.filter_collection = self.filter_collection.tolist()
        except:
            print("Oops, can't open file")
            a = False
        return a

    def get_filters(self) -> List:
        print("FilterReader get_filters")
        return self.filter_collection

if __name__ == '__main__':
    path = "..\\..\\resources\\csv\\AH_tobe.csv"
    A = FilterReader()
    A.open_file(path)
    print(A.get_filters())
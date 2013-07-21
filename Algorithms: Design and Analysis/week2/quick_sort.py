#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

class QuickSortArray:
    def __init__(self):
        self.f = open('quick_sort_input')
        self.f.seek(0)
        self.array =map(self.toInt, self.f.read().splitlines()) 
        self.f.close()
        self.nb_of_comparison = 0

    def toInt(self, x):
        return int(x)

    def sort(self, array = None):
        if array == None:
            array = self.array
        return self.partition(array)

    def partition(self, array):
        sorted_array = []
        if len(array) == 0:
            return sorted_array
        if len(array) == 1:
            return array
        self.nb_of_comparison += len(array) - 1
        i = 1
        pivot = array[0]
        for j in range(1, len(array)):
            if  pivot > array[j]:
                self.swap(array, j, i)
                i += 1
        self.swap(array, 0, i-1)
        sorted_array.extend(self.partition(array[0:i-1]))
        sorted_array.append(array[i-1])
        sorted_array.extend(self.partition(array[i:]))

        return sorted_array
    
    def swap(self, array, i, j):
        t = array[i]
        array[i] = array[j]
        array[j] = t
        return array

if __name__ == "__main__":
    t = QuickSortArray() 
    print t.sort()
    print t.nb_of_comparison

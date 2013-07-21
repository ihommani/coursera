#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

class QuickSortArray:
    def __init__(self, strategy = 1):
        self.f = open('quick_sort_input')
        self.f.seek(0)
        self.array =map(self.toInt, self.f.read().splitlines()) 
        self.f.close()
        self.nb_of_comparison = 0
        self.strategy = strategy
        self.strategies = {1: "FIRST", 2: "LAST", 3: "MEDIAN"}

    def toInt(self, x):
        return int(x)

    def sort(self, array = None, pivot_position = 0):
        if array == None:
            array = self.array
        return self.partition(array, self.strategy)

    def partition(self, array, strategy = 1):
        sorted_array = []
        if len(array) == 0:
            return sorted_array
        if len(array) == 1:
            return array
        self.nb_of_comparison += len(array) - 1
        i = 1
        pivot = self.define_pivot(array, self.strategy)
        index_pivot = array.index(pivot)
        
        self.swap(array, index_pivot, 0)
        for j in range(1, len(array)):
            if  pivot > array[j]:
                self.swap(array, j, i)
                i += 1
        self.swap(array, index_pivot, i-1)
        sorted_array.extend(self.partition(array[0:i-1], strategy))
        sorted_array.append(array[i-1])
        sorted_array.extend(self.partition(array[i:], strategy))
        return sorted_array

    def define_pivot(self, array, strategy):
        if self.strategies[strategy] == "FIRST":
            return array[0]
        elif self.strategies[strategy] == "LAST":
            return array[len(array) - 1]
        elif self.strategies[strategy] == "MEDIAN":
            if len(array) % 2 == 1: 
                return self.median_of_three(array[0], array[len(array)/2], array[len(array)-1])
            else:
                return self.median_of_three(array[0], array[(len(array)/2) - 1], array[len(array)-1])
            return array
        else:
            return

    def median_of_three(self, a, b, c):
        t = [a, b, c]
        t.sort()
        return t[len(t)/2]
    
    def swap(self, array, i, j):
        if i == j:
            return
        t = array[i]
        array[i] = array[j]
        array[j] = t
        return array

if __name__ == "__main__":
    t = QuickSortArray(1) 
    print t.sort()
    print t.nb_of_comparison

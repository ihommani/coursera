#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

class MergeArray:

    def __init__(self):
        self.inversions = 0
        self.f = open('merge_sort_input')
        self.f.seek(0)
        self.array =map(self.toInt, self.f.read().splitlines()) 
        self.f.close()

    def toInt(self, x):
        return int(x)

    def sort(self, array = None):
        if array == None:
            array = self.array

        if len(array) > 2:
            return self.merge(self.sort(array[:len(array)/2]), self.sort(array[len(array)/2:]))
        return self.swap(array)

    def merge(self, array1, array2):
        array3 = []
        for k in range(len(array1) + len(array2)):    
            if len(array1) == 0 and len(array2) > 0:
                array3.append(array2.pop(0))
            elif len(array2) == 0 and len(array1) > 0:
                array3.append(array1.pop(0))
            elif array1[0] < array2[0]:
                array3.append(array1.pop(0))
            else:
                array3.append(array2.pop(0))
                self.inversions += len(array1)
        return array3

    def swap(self, array):
        if len(array) == 1:
            return array
        elif array[0] > array[1]:
            temp = array[1]
            array[1] = array[0]
            array[0] = temp
            self.inversions += 1
        return array     

#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

class Result:
    def __init__(self, inversions, merged_array):
        self.inversions=inversions

class MergeArray:

    def sort(self, array):
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
        return array3

    def swap(self, array):
        if len(array) == 1:
            return array
        elif array[0] > array[1]:
            temp = array[1]
            array[1] = array[0]
            array[0] = temp
        return array     


if __name__ == "__main__":
    t = [341, 2, 6, 434, 23, 45, 5, 7, 12]
    t = MergeArray().sort(t)
    print t
    
    


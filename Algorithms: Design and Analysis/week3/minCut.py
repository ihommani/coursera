
#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

import random

class Contraction:
    def __init__(self, strategy = 1):
        self.f = open('minCut_input')
        self.f.seek(0)
        self.adjencyList = self.__computeAdjencyList()
        self.f.close()
        self.removedItems = {}

    def __toInt(self, x): 
        return int(x)

    def __computeAdjencyList(self):
        d = {}
        lines = self.f.readlines();
        for line in lines:
            l = map(self.__toInt, line.split())
            d[l.pop(0)] = l
        return d

    def __doContraction(self, x, y):
        self.removedItems[y] = x
        d = self.adjencyList.pop(y)
        self.adjencyList[x].extend(d)

    def __fusedNodeAlias(self, node):
        if node in self.removedItems.keys():
            return self.__fusedNodeAlias(self.removedItems[node])
        else:
            return node

    def __computeNumberOfCut(self):
        count = 0
        keys = self.adjencyList.keys()
        nodes = self.adjencyList[keys[0]]
        for node in nodes: 
            if keys[0] != self.__fusedNodeAlias(node):
                count += 1
        return count
                    
    def computeMinCut(self):
        while len(self.adjencyList.keys()) > 2: 
            node = random.choice(self.adjencyList.keys())
            nodeToFuse = node
            # We cannot fuse with ourself
            while node == nodeToFuse:
                nodeToFuse = self.__fusedNodeAlias(random.choice(self.adjencyList[node]))
            self.adjencyList[node]
            self.__doContraction(node, nodeToFuse)
        return self.__computeNumberOfCut()
            

if __name__ == "__main__":
    a = Contraction()
    lista = []
    print a.computeMinCut()
    
    for i in range(3):
        print a.computeMinCut()

import random


class Heap:

    def __init__(self ):
        self.heap = []

    def __init__(self, arr):
        self.heap = list.copy(arr)
        self.buildHeap()

    @staticmethod
    def parent (index):
        return (index-1) // 2
    @staticmethod
    def left(index):
        return 2*index + 1
    @staticmethod
    def right(index):
        return 2*index + 2
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def filterUp(self, index):
        while self.heap[index] > self.heap[Heap.parent(index)]:
            self.swap(index, Heap.parent(index))
            index = Heap.parent(index)
    def filterDown(self, index):
        left = Heap.left(index)
        right = Heap.right(index)
        if left < len(self.heap) and self.heap[index] < self.heap[left]:
            largest = left
        else:
            largest = index

        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        if (largest != index):
            self.swap(index, largest)
            self.filterDown(largest)


    def insert (self, value):
        self.heap.append(value)
        self.filterUp(len(self.heap) - 1)
    def extractMax(self):
        if len(self.heap) == 0:
            return
        self.swap(0, len(self.heap)-1)
        r = self.heap.pop()
        self.filterDown(0)
        return r

    def find(self):
        return

    def delete (self, value):
        return

    def buildHeap(self):
        for i in range((len(self.heap) - 2)//2, -1, -1):
            self.filterDown(i)

    def heapSort(self):
        arr = []
        for i in range (len(self.heap)):
            arr.append(self.extractMax())
        return arr

arr = [19, 87, 31, 37, 8, 52, 33, 33, 77, 6]
hArr = Heap(arr)
print(hArr.heapSort())
print(hArr.heap)


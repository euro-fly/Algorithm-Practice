import math

def floor(a):
    return int(math.floor(a))

def swap(myList, a, b):
    myList[a], myList[b] = myList[b], myList[a]

def max_heapify(heap, index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2
    if left < len(heap) and heap[left] > heap[largest]:
        largest = left
    if right < len(heap) and heap[right] > heap[largest]:
        largest = right
    if largest != index:
        swap(heap, index, largest)
        max_heapify(heap, largest)

def build_heap(heap):
    for i in xrange(floor(len(heap)/2), -1, -1):
        max_heapify(heap, i)

def heapsort(heap, count=len(heap)):
    


test1 = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

#EXPECTED: [ 16, 14, 9, 10, 7, 8, 3, 1, 4, 2 ]
# OR: [ 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 ]
build_heap(test1)

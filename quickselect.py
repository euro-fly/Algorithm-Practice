import random
import time

#QUICKSELECT
#Both in-place and not-in-place
#By Jacob Madrid

def swap(myList, x, y):
    myList[x], myList[y] = myList[y], myList[x]

def partition(myList, start, end):
    pivot = myList[end]
    i = start
    for j in xrange(start, end-1, 1):
        if myList[j] <= pivot:
            swap(myList, i, j)
            i+=1
    swap(myList, i, end)
    return end

def quickselect(myList, k):
    left = []
    right= []
    pivot = myList[random.randint(0, len(myList) - 1)]
    for element in myList:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    if len(left) == k - 1: #if there are exactly k-1 elements smaller than the pivot
        return pivot #pivot is therefore the kth smallest, return it
    elif len(left) >  k - 1: #but if the left partition is larger or equal to k, then it still contains k
        return quickselect(left, k)
    elif len(left) < k - 1: #but if not, then... it's in the right partition
        return quickselect(right, k)
    else:
        return False

    
def quickselectInPlace(myList, start, end, k):
    pivot = partition(myList, start, end)
    if start < end:
        if len(myList[start:pivot]) == k:
            return myList[pivot]
        elif len(myList[start:pivot]) > k:
            return quickselectInPlace(myList,start,pivot - 1, k)
        else:
            return quickselectInPlace(myList,pivot + 1, end, k)
    else:
        return
        
def selectInPlace(myList, k):
	return quickselectInPlace(x, 0, len(x) - 1, k)



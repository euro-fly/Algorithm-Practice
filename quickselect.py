import random

# finds the kth smallest element in myList
# myList is assumed to be unsorted.
def quickselect(myList, k):
    left = []
    right= []
    pivot = myList.pop(random.randint(0, len(myList)))
    for element in myList:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    if len(left) + 1 == k: #if there are exactly k-1 elements smaller than the pivot
        return pivot #pivot is therefore the kth smallest, return it
    elif len(left) + 1 >  k: #but if the left partition is larger or equal to k, then it still contains k
        return quickselect(left, k)
    else: #but if not, then... it's in the right partition
        return quickselect(right, k)

randomList = [7, 10, 4, 3, 20, 15]

import random
import time

#QUICKSELECT
#Both in-place and not-in-place
#By Jacob Madrid

def partition(myList, start, end):
    pivot = myList[random.randint(start,end)]
    myList[pivot], myList[start] = myList[start], myList[pivot]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right                             # Return the split point


## THE BELOW CODE IS BROKEN. I'm still fixing this...

##def quickselect(myList, k):
##    left = []
##    right= []
##    pivot = myList[random.randint(0, len(myList) - 1)]
##    for element in myList:
##        if element <= pivot:
##            left.append(element)
##        else:
##            right.append(element)
##    if len(left) == k - 1: #if there are exactly k-1 elements smaller than the pivot
##        return pivot #pivot is therefore the kth smallest, return it
##    elif len(left) >  k - 1: #but if the left partition is larger or equal to k, then it still contains k
##        return quickselect(left, k)
##    else: #but if not, then... it's in the right partition. find the k - len(left)th element.
##        return quickselect(right, (k - len(left) + 1))

    
def quickselectInPlace(myList, start, end, k):
    if k == 0:
        return False
    pivot = partition(myList, start, end)
    if start < end:
        if pivot == k - 1: # Because we know that the element at index pivot is already sorted, just check it vs. k-1
            return myList[pivot]
        elif pivot > k - 1:
            return quickselectInPlace(myList,start,pivot - 1, k)
        else:
            return quickselectInPlace(myList, pivot + 1, end, k - len(myList[start:pivot]))
    else:
        return myList[end]
        
def selectInPlace(myList, k):
	return quickselectInPlace(myList, 0, len(myList) - 1, k)



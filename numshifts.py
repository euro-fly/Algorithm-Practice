def _numShifts(myList, start, end):
    midpoint = int((start + end) / 2)
    left = midpoint - 1
    right = midpoint + 1
    if myList[midpoint] < myList[left]:
        return midpoint
    elif myList[midpoint] > myList[right]:
        return right
    else:
        if myList[midpoint] < myList[end]: #sequence from midpoint is monotonic, check from start to MP
            return _numShifts(myList, start, midpoint)
        else:
            return _numShifts(myList, midpoint, end)
    
def numShifts(myList):
    return _numShifts(myList, 0, len(myList) - 1)

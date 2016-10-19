# FUNCTION ONE: Output the largest increasing sequence in a given list
# If multiple sequences have the same length, you can output any of them

def sequence_length(x, y):
    return y - x + 1

def largest_sequence(my_list):
    biggest_start = 0
    biggest_end = 0
    current_start = 0
    current_end = 0
    for i in xrange(0, len(my_list) - 1, 1):
        if my_list[i] > my_list[current_end]:
            current_end = i
            if sequence_length(current_start, current_end) > sequence_length(biggest_start, biggest_end):
                biggest_start = current_start
                biggest_end = current_end
        elif my_list[i] < my_list[current_end]:
            # if our new element is less than the end of our sequence, terminate it. start fresh from i.
            current_start = i
            current_end = i
        if sequence_length(biggest_start, biggest_end) > (len(my_list) - i) and current_start > biggest_start:
            # if our largest sequence is larger than the number of elements left in the list, and we're starting a new sequence somewhere past it... we're done.
            break
    return my_list[biggest_start:biggest_end+1]


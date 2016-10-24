def numVowels(string):
    vowels = 0
    consonants = 0
    for char in string:
        if char in "aeiouAEIOU":
            vowels +=1
    return vowels

def equalVowels(string):
    for j in xrange(len(string), 1, -1):
        for i in xrange(0, len(string), 1):
            my_substring = string[i:i+j]
            print my_substring
            print i, j+1
            num_vowels = numVowels(my_substring)
            if (num_vowels == len(my_substring) - num_vowels):
                return my_substring
            
    return False
            

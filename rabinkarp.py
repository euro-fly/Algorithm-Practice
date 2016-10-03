# RABIN-KARP IMPLEMENTATION
# TODO: maybe come up with a better hash() than Python's own
# TODO: maybe figure out how to do all the comparisons in one without iterating through a list

def isSubstringPresent(pattern, test, caseSensitive = True):
    if not caseSensitive:
        pattern = pattern.lower()
        test = test.lower()
    if len(pattern) > len(test):
        return False
    elif len(pattern) == len(test):
        return pattern == test
    else:
        patternHash = hash(pattern)
        for i in xrange(0, (len(test) - len(pattern)), 1):
            testHash = hash(test[i:i+len(pattern)])        
            if patternHash == testHash:
                if pattern == test[i:i+len(pattern)]:
                    return i
        return False

def areSubstringsPresent(patterns, test, caseSensitive = True):
    substrings = []
    for pattern in patterns:
        substrings.append(isSubstringPresent(pattern, test, caseSensitive))
    return substrings

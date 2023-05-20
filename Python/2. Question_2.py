def is_valid(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    values = list(freq.values())
    values_set = set(values)
    if len(values_set) == 1:
        return "YES"
    elif len(values_set) == 2:
        max_value = max(values)
        min_value = min(values)
        if values.count(max_value) == 1 and max_value - min_value == 1:
            return "YES"
        elif values.count(min_value) == 1:
            return "YES"
    return "NO"

s = "aabbccddeef"
print(is_valid(s))
   #This string is valid because we can remove one occurrence of f and the remaining characters will occur the same number of times. The Output is "YES"


#Given Below are Additional Test Cases
s1 = "aabbcdde"
print(is_valid(s1))
   #The Output is "NO"
s2 = "aaaabbbbcccc"
print(is_valid(s2))
    #The Output is "YES"
s3 = "aaaabbbbccccc"
print(is_valid(s3))
    #The Output is "YES"

#Explanation

''' 
1. s1 = "aabbcdde"
    This string is not valid because we can remove only one occurrence of c but that still leaves character frequencies of { "a": 2, "b": 2 , "c": 0, "d": 2 }. The function returns "NO".

2. s2 = "aaaabbbbcccc"
    This string is valid because all characters occur the same number of times. The function returns "YES".

3. s3 = "aaaabbbbccccc"
    This string is valid because we can remove one occurrence of c and the remaining characters will occur the same number of times. The function returns "YES".

'''
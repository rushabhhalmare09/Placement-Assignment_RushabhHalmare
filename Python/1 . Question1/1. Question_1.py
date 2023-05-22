def highest_frequency_word(string):
    words = string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    max_count = max(word_count.values())
    max_word = [word for word in word_count if word_count[word] == max_count][0]
    return len(max_word)

string = "write write write all the number from from from 1 to 100"
print(highest_frequency_word(string))
#Output-> which is the length of the highest-frequency word write.


#Given Below are additional Test Cases

#1.
string1 = "one two three four five six seven eight nine ten one two three"
print(highest_frequency_word(string1))
  #The output is 3.

#2.
string2 = "appl banana appl orange banana appl"

print(highest_frequency_word(string2))
   #The output is 4

#3.
string3 = "The quick brown fox jumps over the lazy dog"
print(highest_frequency_word(string3))
    #The output is 3.


#Explanation

''' 
1.string1 = "one two three four five six seven eight nine ten one two three"
    The highest-frequency words are one, two, and three, which all appear 2 times. The length of these words is 3, so the output is 3.

2.string2 = "appl banana appl orange banana appl"
   The highest-frequency word is appl, which appears 3 times. The length of appl is 4, so the output is 4

3.string3 = "The quick brown fox jumps over the lazy dog"
    All words in this string appear only once, so any word can be considered the highest-frequency word. The length of the first word The is 3, so the output is 3.

'''
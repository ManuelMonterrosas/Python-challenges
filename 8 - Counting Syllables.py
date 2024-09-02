'''
Define a function named count that takes a single parameter. The parameter is a string. 
The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
'''

def count(s):
    number = 1
    for i in range(len(s)):
        if s[i] == "-":
            number += 1
    return number

print(count("ho-tel"))

'''
Feedback: There are three solutions in the website. The "naive" one is similar to mine.
The other two use smarter, python-specific methods like count and split.

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))
'''
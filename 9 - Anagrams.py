'''
Two strings are anagrams if you can make one from the other by rearranging the letters.
Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.
For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
'''

# First try. Failed since it returns true for is_anagram("test","tess"). Having the same letters is not enough, I must count them too
#def is_anagram(s1, s2):
#    return all([i in s2 for i in s1])

def is_anagram(s1, s2):
    return all([s1.count(i)==s2.count(i) for i in s1])

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))

'''
Feedback: the easiest solution was to sort both strings and compare them with a simple a == b

# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
'''
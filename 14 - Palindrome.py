'''
A string is a palindrome when it is the same when read backwards.
For example, the string "bob" is a palindrome. So is "abba". 
But the string "abcd" is not a palindrome, because "abcd" != "dcba".
Write a function named palindrome that takes a single string as its parameter. 
Your function should return True if the string is a palindrome, and False otherwise.
'''

def palindrome(s):
    return s==s[::-1]

print(palindrome('bob'))
print(palindrome('abcd'))

'''
Feedback: out of the three given solutions, mine matches the smarter solution.
The longest one consists on looping forwards and backwards along the string as you compare element-wise.
The one I found interesting is this recursive one

# recursive solution: equivalent to looping.
def palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])
'''
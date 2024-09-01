'''
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def mid(s):
    if len(s)%2 == 0: # If we have even number of characters
        mid_value = ''
    else:
        mid_value = s[int(len(s)/2)]
    return mid_value

print(mid('abc'))
print(mid('aaaa'))

'''
Feeback: the website suggests the answer

def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

Which is equivalent to mine except for the fact that they return inside and if. 
I personally prefer to single-return style.
'''
'''
Write a function named add_dots that takes a string and adds "." in between each letter. 
For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
'''
# IMPORTANT: the dots should be in between the letters, not after them. That means, we don't end with a dot.
def add_dots(s):
    new_s = ''
    for i in range(len(s)-1):
        new_s = new_s + s[i] + '.'
    new_s = new_s + s[-1]
    return new_s

def remove_dots(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] != '.':
            new_s = new_s + s[i]
    return new_s

print(add_dots('test'))
print(remove_dots('t.e.s.t'))

'''
Feedback: the website provides two solutions, a long one and a short one. My method is basically the long solution.
For the short one they wrote

# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")

Using replace is nice. Join is a method I did not know.
'''
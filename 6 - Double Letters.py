'''
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. 
The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
'''

def double_letters(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return True
    return False

print(double_letters('hello'))
print(double_letters('nono'))

'''
Feedback: the website provides two solutions. 
The long one is similar to mine but slightly longer, since it defines letter 1 and letter 2, and then compares them.
The short one is interesting because it uses list comprehension, zip and the logical function any

def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])

It basically puts in pairs the consecutive strings, and then it just checks if any of the pairs are double.    
'''
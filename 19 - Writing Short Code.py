'''
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.
'''

def convert(list):
    return [str(i) for i in list]

print(convert([1, 2, 3]))

'''
Feedback: my solution matches one of the given ones. The other solution uses map

# using map
def convert(ns):
    return list(map(str, ns))
'''
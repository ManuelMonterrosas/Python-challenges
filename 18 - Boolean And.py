'''
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
'''

def triple_and(a, b, c):
    return all([a, b, c])

print(triple_and(True, True, True))
print(triple_and(True, True, False))

'''
Feedback: the given solution uses a and b and c insted of all()

def triple_and(a, b, c):
    return a and b and c
'''
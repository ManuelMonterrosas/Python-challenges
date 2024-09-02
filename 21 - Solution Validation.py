'''
The aim of this challenge is to write code that can analyze code submissions. 
We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
'''

def validate(str):
    if 'def' not in str:
        return 'missing def'
    if ':' not in str:
        return 'missing :'
    if '(' not in str or ')' not in str:
        return 'missing paren'
    if '('+')' in str:
        return 'missing param'
    if '    ' not in str:
        return 'missing indent'
    if 'validate' not in str:
        return 'wrong name'
    if 'return' not in str:
        return 'missing return'
    return True

'''
Feedback: my solution matches the given one.
'''
'''
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
'''
option = 3

if option == 1:
    # My first try. It fails when giving strings because int(string) is not defined
    def only_ints(a, b):
        if int(a) == a and int(b) == b:
            return True # I gave into the return inside if for simplicity hehe
        return False

if option == 2:
    # my second try using try, except. This works for the two given examples, but still fails for (1, True), since it returns True.
    def only_ints(a, b):
        try:
            if int(a) == a and int(b) == b:
                return True
        except:
            return False
        
if option == 3:
    # my third try. This time I will use type(a) and compare to a type I already know to be int.
    def only_ints(a, b):
        if type(a) == type(1) and type(b) == type(1):
            return True
        return False

print(only_ints(1,2))
print(only_ints('a', 1))

'''
Feedback: from the provided solution I learned that I can directly use bool and bool directly on the return

def only_ints(a, b):
    return type(a) == int and type(b) == int
'''

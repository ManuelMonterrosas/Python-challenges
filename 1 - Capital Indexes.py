'''
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

# I can think of at least two ways of solving this
option = 2
if option == 1: # First method
    # Very rustic. Provide a list of capitals, then test the elements in the string against the elements in the list
    # This wil fail if non-english letters are used, and is prone to human mistake when making the list.
    list_capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def capital_indexes(some_string):
        positions = []
        for i in range(len(some_string)):
            if some_string[i] in list_capital_letters:
                positions.append(i)
        return positions

if option == 2: # Second method
    # Smarter method. Make all letters on the string capital letters and return the positions that match the original string
    def capital_indexes(some_string):
        positions = []
        capital_string = some_string.upper()
        for i in range(len(some_string)):
            if some_string[i] == capital_string[i]:
                positions.append(i)
        return positions
     
print(capital_indexes('HeLlO'))

'''
Feedback: the website also shows two possible solutions similar to yours.

For option one, you don't need to build the capital letters as a list. 
A simple "ABCDEFGHIJKLMNOPQRSTUVWXYZ" would be enough to compare.

For option two, if s is the string, a more compact solution is return [i for i in range(len(s)) if s[i].isupper()].
But some readability is sacrificed in my opinion.
'''
'''
Write a function that takes a list of lists and flattens it into a one-dimensional list.
Name your function flatten. It should take a single parameter and return a list.
For example, calling:
flatten([[1, 2], [3, 4]])
Should return the list:
[1, 2, 3, 4]
'''

def flatten(og_list):
    flat_list = []
    for i in range(len(og_list)): # this will work only for 2-d matrices
        for j in range(len(og_list[i])):
            flat_list.append(og_list[i][j])
    return flat_list

print(flatten([[1,2],[3,4]]))

'''
Feedback: my solution matched the naive solution. A more advanced solution is given using nested list comprehensions.
It is certainly more concise but the idea is the same: loop twice and return all. It will still fail with higher order lists.

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
'''
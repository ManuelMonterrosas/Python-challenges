'''
Define a function named largest_difference that takes a list of numbers as its only parameter.
Your function should compute and return the difference between the largest and smallest number in the list.
For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
You may assume that no numbers are smaller or larger than -100 and 100.
'''

def largest_difference(list):
    return max(list)-min(list)

print(largest_difference([1, 2, 3]))

'''
Feedback: here I gave the short solution. The naive solution involved looping through the list to find the max and min.
'''
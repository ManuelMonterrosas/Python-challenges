'''
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
Your code should find the biggest number of consecutive zeros in the string. 
For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. 
Your function should return the number described above.
'''

def consecutive_zeros(s):
    return max([lengths
        for slices in s.split('1') 
        for lengths in [len(slices)]])

print(consecutive_zeros("1001101000110"))

'''
Feedback: out of the two given solutions, my solution is similar to the shorter one, but I have used an extra for loop.
The longer solution loops while counting 0 streaks.
The shorter solution uses split with "1" and then finds the maximum length.

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
'''
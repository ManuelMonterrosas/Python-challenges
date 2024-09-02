'''
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
'''

# this approach is messy and requires a lot of ifs
'''
def format_number(num):
    result = '' # string to carry the answer. We will start from the end backwards and flip the string when we are done
    reversed = str(num)[::-1] # here is the reversed string
    for i in range(3, len(reversed), 3): # i contains already the positions where the commas should g
        #print(i)
        result = result + reversed[i-3:i] + ',' # add what we had already, plus the new set of numbers plus the comma
    #result = result + reversed[i:] # in the end the leftover without comma after them. This line fails when number with less than 4 digits since i is not defined
    result = result + str(num)[len(str(num))%3::-1]
    return result[::-1] # do not forget to flip
'''

# try again in a simpler way
def format_number(num):
    reversed = str(num)[::-1] # reversed string
    result = ''
    # we are going to add commas when the position is a multiple of 3, except for 0
    for i in range(len(reversed)):
        if i%3 == 0 and i>0: # here we add comma
            result = result + ',' + reversed[i]
        else: # here we don't add comma
            result = result + reversed[i]
    return result[::-1] # reverse the string again to get the answer

print(format_number(1))
print(format_number(1000000))
print(format_number(1234567))

'''
Feedback: my solution was almost exactly the same as the DIY solution given in the website.
A much simpler solution uses the built-in format giver.

# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
'''
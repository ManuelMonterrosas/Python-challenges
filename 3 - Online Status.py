'''
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.
'''

def online_count(online_dict):
    people_online = 0
    for i in range(len(online_dict)):
        if list(online_dict.values())[i] == 'online':
            people_online = people_online + 1
    return people_online

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))

'''
Feedback: The website provides a long answer and a short answer.

# long version
def online_count(people):
    count = 0
    for person, status in people.items():
        if status == "online":
            count += 1
    return count

From the long version I like that they used the double-valued .items(). 
Person is unnecessary in this case but it could be useful. 

# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])

From the short version I don't understand how the p is defined.
'''
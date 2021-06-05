# You are given an array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight
# of those people is at most limit.

# Return the minimum number of boats to carry every given person
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

def numRescueBoats(people, limit):
    i, j = 0, len(people) - 1
    cnt, temp, = 0, 0
    people.sort()
    while i <= j:
        if people[i] <= limit - people[j]:
            i += 1
            j -= 1
        else:
            j -= 1
        cnt += 1
    return cnt


print(numRescueBoats([3,5,3,4], 5))
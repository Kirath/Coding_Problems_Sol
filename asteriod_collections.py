# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet,
# the smaller one will explode. If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.


# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

def asteroidCollision(asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans


print(asteroidCollision([5,10,-5]))
# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means
# empty and 1 means not empty, and an integer n, return if n new
# flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

def canPlaceFlowers(flowerbed, n: int):
    i = 0
    if len(flowerbed) < 2:
        if flowerbed[0] == 0:
            n -= 1

    else:
        while i <= len(flowerbed) - 1 and n > 0:
            if flowerbed[i] == 1:
                i += 1

            elif flowerbed[i] == 0 and i != 0 and i < len(flowerbed) - 1 and flowerbed[i + 1] == 0 and flowerbed[
                i - 1] == 0:
                flowerbed[i] = 1
                i += 2
                n -= 1
            elif flowerbed[i] == 0 and i == 0 and flowerbed[i + 1] == 0:
                i += 2
                n -= 1
            elif flowerbed[len(flowerbed) - 1] == 0 and i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                n -= 1
                break


            else:
                i += 1

    if n > 0:
        return False
    else:
        return True


print(canPlaceFlowers([1,0,0,0,1], 1))
# Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.
# Where:
# A[i][0] = start time of the ith meeting.
# A[i][1] = end time of the ith meeting.
# Find the minimum number of conference rooms required so that all meetings can be done.

def solve(A):
    arr = []
    max_c = 0
    temp = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j == 0:
                arr.append((A[i][j], 'A'))
            else:
                arr.append((A[i][j], 'D'))
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i][0] == arr[i + 1][0]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # print(arr)
    for i in range(len(arr)):
        if arr[i][1] == 'A':
            temp += 1
            if max_c < temp:
                max_c = temp
        else:
            temp -= 1
            if max_c < temp:
                max_c = temp
    return max_c


print(solve([
  [7, 10],
  [4, 19],
  [19, 26],
  [14, 16],
  [13, 18],
  [16, 21]
]))
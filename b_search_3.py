def find_ele_b(arr, k):

    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < k:
            low = mid + 1
        if arr[mid] > k:
            high = mid - 1
        elif arr[mid] == k:
            if (mid > 0) and mid < len(arr) - 1 and (arr[mid + 1] != k and arr[mid - 1] != k):
                return arr[mid]
    return -1


k = int(input())
arr = list(map(int,input().split()))
print(find_ele_b(arr, k))

def max_heapify(arr, i):
    N = len(arr)
    if N // 2 < i:
        return
    max_i = i
    if arr[2*i] > arr[max_i]:
        max_i = 2 * i
        print(arr[max_i])
    if (2*i + 1 <= N) and (arr[2*i + 1] > arr[max_i]):
        max_i = 2 * i + 1
        # print(max_i)
    if max_i != i:
        arr[max_i], arr[i] = arr[i], arr[max_i]
        max_heapify(arr, max_i)


def create_max_heap(arr):
    for i in range(1, len(arr) // 2):
        max_heapify(arr, i)
    return arr[1:]


def del_ele(arr, ind):
    arr[ind] = float('inf')
    for i in range(1, len(arr) // 2):
        max_heapify(arr, i)
    # print(arr)
    for i in range(2, len(arr) // 2):
        max_heapify(arr, i)
    return arr[2:]


arr = ['Na', 50, 6, 8, 9, 10]
arr.append(5)
print(create_max_heap(arr))
print(del_ele(arr, 2))

def c_sort(arr):
    c_arr = [0] * (len(arr) + max(arr))
    # print(c_arr)
    output = [0] * len(c_arr)
    prefix = [0] * len(c_arr)
    for i in range(len(arr)):
        c_arr[arr[i]] += 1
    for i in range(1, len(c_arr)):
        prefix[i] += c_arr[i] + prefix[i - 1]
    # print(prefix)
    for i in range(len(arr)):
        output[prefix[arr[i]] - 1] = arr[i]
        prefix[arr[i]] -= 1
    return output

arr = list(map(int,input().split()))
print(c_sort(arr))
def pairs(k, arr):
    length = len(arr)
    count = 0
    for i in range(length):
        for j in range(length):
            if i != j:
                if arr[i] - arr[j] == k:
                    count += 1
    return count


array = [1, 2, 3, 4]
a = pairs(1, array)
print(a)

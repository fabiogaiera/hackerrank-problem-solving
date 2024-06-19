def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr)

    minimum = 0
    for i in range(length - 1):
        minimum += sorted_arr[i]

    maximum = 0
    for i in range(1, length):
        maximum += sorted_arr[i]

    print(minimum, maximum)


array = [4, 5, 2, 1, 3]
miniMaxSum(array)

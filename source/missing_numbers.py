def missingNumbers(arr, brr):
    dct_arr = {}
    dct_brr = {}

    for elem in arr:
        if elem not in dct_arr:
            dct_arr[elem] = 1
        else:
            dct_arr[elem] += 1

    for elem in brr:
        if elem not in dct_brr:
            dct_brr[elem] = 1
        else:
            dct_brr[elem] += 1

    array_missing_numbers = []

    for elem in brr:
        if elem not in arr:
            array_missing_numbers.append(elem)
        # If elem is in arr
        else:
            if dct_arr[elem] != dct_brr[elem]:
                array_missing_numbers.append(elem)

    return sorted(set(array_missing_numbers))


arr1 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
arr2 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

arr3 = missingNumbers(arr1, arr2)
print(arr3)

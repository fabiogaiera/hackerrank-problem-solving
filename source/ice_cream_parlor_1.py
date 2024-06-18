def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == m:
                    return [i + 1, j + 1]

    return None


array = [1, 2, 3, 4, 5, 6]

result = icecreamParlor(6, array)
print(result)

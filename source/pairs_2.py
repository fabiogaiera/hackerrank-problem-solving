def count_pairs_with_difference(arr, target):
    # Set to store the elements we've seen so far
    seen = set()
    # Counter for the number of pairs
    count = 0

    for num in arr:
        # Check if there is a number in the set such that their difference is the target
        if num - target in seen:
            count += 1
        if num + target in seen:
            count += 1

        # Add the current number to the set
        seen.add(num)

    return count


# Example usage:
array = [1, 5, 3, 4, 2]
tgt = 2
print(count_pairs_with_difference(array, tgt))  # Output should be 3

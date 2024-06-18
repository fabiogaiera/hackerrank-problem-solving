def iceCreamParlor(cost, m):
    # Dictionary to store the index of each price
    price_indices = {}

    for i, price in enumerate(cost):
        # Calculate the complement that, when added to the current price, equals m
        complement = m - price

        # Check if the complement is already in the dictionary
        if complement in price_indices:
            # Return the 1-based indices of the two flavors
            return [price_indices[complement] + 1, i + 1]

        # Add the current price and its index to the dictionary
        price_indices[price] = i

    return None


# Example usage
m = 6
cost = [1, 3, 4, 5, 6]
result = iceCreamParlor(cost, m)
print(result)  # Output should be [1, 4]

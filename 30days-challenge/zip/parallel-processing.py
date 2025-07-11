# Calculate totals from multiple lists
prices = [10.99, 15.50, 8.75, 22.00]
quantities = [2, 1, 3, 1]

totals = [price * qty for price, qty in zip(prices, quantities)]
print(totals)  # [21.98, 15.5, 26.25, 22.0]

# Or using map
totals = list(map(lambda x: x[0] * x[1], zip(prices, quantities)))
print(totals)  # [21.98, 15.5, 26.25, 22.0]

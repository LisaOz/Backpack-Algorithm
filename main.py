'''
This code demonstrates a 'Backpack Algorithm' that is a classic optimisation problem.
The aim is to pack a backpack with the most valuable combination of items
without exceeding the backpack's weight capacity.
Each item can either be taken or not taken (no fractions allowed).
The problam is solved using dynammic programming approach.
'''


def backpack(values, weights, capacity):
    n = len(values)  # Calculate the number of items n in the values list
    dp = [[0] * (capacity + 1) for i in range (n + 1)]  # Initialise a 2D list to store the maximum value

    # loop to iterate through each item i of the list
    for i in range (1, n + 1):

        # Loop iterates through each possible weight capacity
        for w in range(1, capacity + 1):

            # Check if the weight of the current item <= current capacity
            if weights[i - 1] <= w:

                # Update the value: either take the max value and include the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]]+ values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w] # or exclude the item: value remains the same without the current item
    return dp[n][capacity]


if __name__ == "__main__":
    values = [50, 60, 100]
    weights = [10, 20, 30]
    capacity = 70
    print("Maximum value in the backpack:", backpack(values, weights, capacity))
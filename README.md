# Backpack-Algorithm

The Backpack Algorithm is a well-known optimisation problem, where the goal is to choose items to maximise their value  while staying within the given weight capacity.

## Algorithm Explanation

The solution to the backpack problem using dynamic programming involves creating a 2D array **'dp'** where **dp[i][w]** represents the maximum value that can be reached with the first **[i]** items and a weight limit of **'w'**.
The algorithm proceeds by considering each item one by one and deciding whether to include it in the backpack or not, based on the maximum value achievable.

## Code Explanation

1. ### Initialisation:
  - **n = len(values)** - Calculate the number of items
  - **'dp = [[0] * (capacity + 1) for i in range(n + 1)**: Initialise a 2D list to store the maximum value.

2. ### Filling the dp Table:
   
   - Loop through each item and weight capacity to fill the **dp** table:     
   - If the current item's weight is less than or equal to the current capacity,
   - update the maximum value by including the item or not;
   - Otherwise, the item is not included. and the current maximum value remains the same.

3. ### Result:
   
The maximum value that can be achieved with the given capacity is stored in **db[n][capacity]**.

## Usage

1. Clone the repository: **https://github.com/LisaOz/Backpack-Algorithm.git**.
2. Run the code: **python.main.py**.

## License
This project us licensed under the MIT License.
   

def knapsack(w, wt, val, n):
    # Create a 2D DP table initialized with 0s
    V = [[0 for j in range(w + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                V[i][j] = 0  # Base Case: 0 items or 0 capacity
            elif wt[i - 1] > j:
                V[i][j] = V[i - 1][j]  # Case: item too heavy
            else:
                V[i][j] = max(V[i - 1][j], val[i - 1] + V[i - 1][j - wt[i - 1]])  # Include or exclude

    return V[n][w]
val = [1,2,3,4]
wt = [3, 4, 5, 6]
w = 8
n = len(val)

print("Optimal Solution:", knapsack(w, wt, val, n))



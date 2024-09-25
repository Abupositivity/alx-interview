#!/usr/bin/python3

"""makeChange function to solve d making change problem"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    # If the total is less than or equal to 0, return 0 as no coins are needed
    if total <= 0:
        return 0

    # Initialize dp array with a large value (infinity) for all totals from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0

    # Iterate over all possible amounts from 1 to total
    for i in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if i - coin >= 0:  # Ensure we are not going below 0
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1, as no combination of coins can make the total
    return dp[total] if dp[total] != float('inf') else -1

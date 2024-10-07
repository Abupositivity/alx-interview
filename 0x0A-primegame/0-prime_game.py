#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x < 1 or not nums:
        return None

    # Precompute prime numbers up to the maximum number in nums using the Sieve of Eratosthenes
    max_n = max(nums)
    primes = [True] * (max_n + 1)  # Create a list of True values for prime number flags
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes to identify prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False  # Mark multiples of i as not prime

    # Calculate the number of prime numbers up to each number from 0 to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner of each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins; if even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

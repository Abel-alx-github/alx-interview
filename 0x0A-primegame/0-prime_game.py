#!/usr/bin/python3
"""Module that define isWinner function."""


def isWinner(x, nums):
    """Function to get who win in prime game"""
    mariWinsSum = 0
    beniWinsSum = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            beniWinsSum += 1
            continue

        isMariaTurns = True

        while (True):
            if not primesSet:
                if isMariaTurns:
                    beniWinsSum += 1
                else:
                    mariWinsSum += 1
                break

            smallestPrime = primesSet.pop(0)
            rounds.remove(smallestPrime)

            rounds = [x for x in rounds if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariWinsSum > beniWinsSum:
        return "Maria"

    if mariWinsSum < beniWinsSum:
        return "Ben"

    return None


def isPrime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if isPrime(n)]
    return primes

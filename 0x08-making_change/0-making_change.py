#!/usr/bin/python3
"""..............Making Change Problem..........."""


def makeChange(coins, total):
    """Determines the fewest number of coins needed \
    to meet a given amount total"""
   
    if total <= 0:
        return 0

    sum_used = 0
    usedcoins = 0
    sorted_coins = sorted(coins, reverse=True)
    for coin in sorted_coins:
        left = (total - sum_used) // coin
        sum_used += left * coin
        usedcoins += left
        if sum_used == total:
            return usedcoins
    return -1
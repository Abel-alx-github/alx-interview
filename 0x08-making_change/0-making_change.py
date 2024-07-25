#!/usr/bin/python3
"""..............Making Change Problem..........."""


def make_change(coins, total):
    """Determines the fewest number of coins needed \
    to meet a given amount total"""
    if total <= 0:
        return 0
    sum = 0
    usedcoins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - sum) // coin
        sum += r * coin
        usedcoins += r
        if sum == total:
            return usedcoins
    return -1

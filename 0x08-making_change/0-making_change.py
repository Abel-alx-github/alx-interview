#!/usr/bin/python3
"""..............Making Change Problem..........."""


def make_change(coins, total):
    """Determines the fewest number of coins needed \
    to meet a given amount total"""
    if total <= 0:
        return 0

    sum_used = 0
    usedcoins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        left = (total - sum_used)
        sum_used += left * coin
        usedcoins += left
        if sum_used == total:
            return usedcoins
    return -1

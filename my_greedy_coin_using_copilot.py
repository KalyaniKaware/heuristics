#!/usr/bin/env python
# use chmod +x file_name.py to make the file a command line function
# to be used for command line tooling
import click

# write a function to that returns quarters and dimes only
def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""
    print(f"Your change for {change}: ")
    coins = [0.25, 0.10]
    coin_lookup = {0.25: "quarter", 0.10: "dime"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict

def greedy_coin_dd(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""
    print(f"Your change for {change}: ")
    coins = [0.10]
    coin_lookup = { 0.10: "dime"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict

# build a command group using click
@click.group()
def main():
    """Return the minimum number of coins for a given change
    Example: ./my_greedy_coin_using_copilot.py 0.99
    """
    pass

# build a click command that returns coins in dimes and quarters
@main.command("dq")
@click.argument("change", type=float)
def dq(change):
    """Return the minimum number of coins for a given change
    Example: ./my_greedy_coin_using_copilot.py dq 0.99 """
    greedy_coin(change)

@main.command("dd")
@click.argument("change", type=float)
def dd(change):
    """Return the minimum number of coins for a given change
    Example: ./my_greedy_coin_using_copilot.py dd 0.99"""
    greedy_coin_dd(change)

# create an entry point
if __name__ == "__main__":
    main()

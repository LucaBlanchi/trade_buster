"""
This module contains various trading strategies.

A strategy is a pure function that takes as input a list of price points (list of floats)
and a wallet object, and returns the amount of cash to be spent (positive) or received
(negative) by selling assets.
"""


def custom_strategy(price_points, wallet):
    # You may implement your own strategy here.
    return 0


def do_nothing_strategy(price_points, wallet):
    """This strategy does nothing. It serves as a placeholder or for testing purposes."""
    return 0


def buy_and_hold_strategy(price_points, wallet):
    """This strategy buys assets at the first opportunity and holds them indefinitely."""
    if wallet.cash > 0:
        return wallet.cash
    return 0


def follow_trend_strategy(price_points, wallet):
    """This strategy follows the trend of the last three price points."""
    if len(price_points) < 3:
        return 0
    uptrend = price_points[-1] > price_points[-2] > price_points[-3]
    downtrend = price_points[-1] < price_points[-2] < price_points[-3]
    return wallet.cash * 0.1 * (uptrend - downtrend)

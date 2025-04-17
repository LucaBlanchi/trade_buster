"""
This module contains various trading strategies.

A trading strategy is a pure function that takes a list of price points (list of floats)
and a wallet object as input, and returns the amount of cash to be spent (positive) or received
(negative) by selling assets.
"""

def customStrategy(pricePoints, wallet):
    # Custom strategy implementation
    return 0

def doNothingStrategy(pricePoints, wallet):
    """This strategy does nothing. It serves as a placeholder or for testing purposes."""
    return 0

def buyAndHoldStrategy(pricePoints, wallet):
    """This strategy buys assets at the first opportunity and holds them indefinitely."""
    if wallet.cash > 0:
        return wallet.cash
    return 0

def followTrendStrategy(pricePoints, wallet):
    """This strategy follows the trend of the last three price points."""
    if len(pricePoints) < 3:
        return 0
    uptrend = pricePoints[-1] > pricePoints[-2] > pricePoints[-3]
    downtrend = pricePoints[-1] < pricePoints[-2] < pricePoints[-3]
    return wallet.cash * 0.1 * (uptrend - downtrend)

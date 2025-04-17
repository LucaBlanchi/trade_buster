# trade_buster

Some (still minimal) functional-oriented code to test algorithmic trading strategies against past price data.

To test a strategy, write a custom strategy function in the `strategies.py` file.

A strategy is a pure function that takes as input a list of price points (list of floats) and a wallet object (defined in `trading.py`, with cash and assets properties), and returns the amount of cash to be spent (positive) or received (negative) by selling assets, according to the last price point (representing the current price for the strategy) and the price history.

It basically decides whether to buy, sell, or hold at that moment according to the current and past prices.

The strategy will be tested by executing `main.py`, recording the wallet history after applying the strategy for each price point.

In `main.py`, you can configure the strategy to test, the initial cash and assets in the wallet, the price points, and the starting price point where the strategy will be applied.

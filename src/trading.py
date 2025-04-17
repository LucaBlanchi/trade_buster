class Wallet:
    def __init__(self, cash, assets):
        self.cash = cash
        self.assets = assets

    def get_worth(self, asset_price):
        return self.cash + self.assets * asset_price


def get_wallet_after_strategy(strategy, price_points, wallet):
    spent_cash = strategy(price_points, wallet)
    new_wallet = Wallet(
        wallet.cash - spent_cash,
        wallet.assets + spent_cash / price_points[-1]
    )
    return new_wallet


def execute_strategy(strategy, price_points, starting_index, wallet):
    wallet_records = [wallet]
    temp_wallet = Wallet(wallet.cash, wallet.assets)

    for i in range(starting_index, len(price_points)):
        temp_wallet = get_wallet_after_strategy(strategy, price_points[:i + 1], temp_wallet)
        wallet_records.append(temp_wallet)

    return wallet_records

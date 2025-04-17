import trading as tr
import strategies as strat
import price_points_constants as ppc


def main():
    starting_wallet = tr.Wallet(cash=1000, assets=0)
    price_points = ppc.SAMPLE_PRICE_POINTS
    starting_index = 0
    strategy = strat.buy_and_hold_strategy

    wallet_records = tr.execute_strategy(
        strategy, price_points, starting_index, starting_wallet
    )

    display_results(price_points, starting_index, wallet_records)


def display_results(price_points, starting_index, wallet_records):
    for record in wallet_records:
        print(f"Cash: {record.cash}, Assets: {record.assets}")

    starting_worth = wallet_records[0].get_worth(price_points[starting_index])
    final_worth = wallet_records[-1].get_worth(price_points[-1])

    print("Final worth:", final_worth)
    print("Gain:", final_worth - starting_worth)
    print("Multiplier:", final_worth / starting_worth)


if __name__ == "__main__":
    main()

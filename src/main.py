import trading as tr
import strategies as str
import price_points_constants as ppc

def main():
    startingWallet = tr.Wallet(1000, 0)
    pricePoints = ppc.SAMPLE_PRICE_POINTS
    strategy = str.buyAndHoldStrategy

    walletRecords = tr.executeStrategy(strategy, pricePoints, 0, startingWallet)
    for record in walletRecords:
        print(f"Cash: {record.cash}, Assets: {record.assets}")
    startingWorth = startingWallet.getWorth(pricePoints[0])
    finalWorth = walletRecords[-1].getWorth(pricePoints[-1])
    print("Final worth: ", finalWorth)
    print("Gain: ", finalWorth - startingWorth)
    print("Multiplier: ", finalWorth / startingWorth)

if __name__ == "__main__":
    main()

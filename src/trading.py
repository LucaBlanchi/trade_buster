class Wallet:
    def __init__(self, cash, assets):
        self.cash = cash
        self.assets = assets
    
    def getWorth(self, assetPrice):
        return self.cash + self.assets * assetPrice

def getWalletAfterStrategy(strategy, pricePoints, wallet):
    spentCash = strategy(pricePoints, wallet)
    newWallet = Wallet(wallet.cash - spentCash, wallet.assets + spentCash / pricePoints[-1])
    return newWallet

def executeStrategy(strategy, pricePoints, startingPricePointPosition, wallet):
    walletRecords = [wallet]
    tempWallet = Wallet(wallet.cash, wallet.assets)

    for i in range(startingPricePointPosition, len(pricePoints)):
        tempWallet = getWalletAfterStrategy(strategy, pricePoints[:i+1], tempWallet)
        walletRecords.append(tempWallet)

    return walletRecords

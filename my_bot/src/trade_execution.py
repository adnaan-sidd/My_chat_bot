async def execute_trade(account, asset, volume, stop_loss, take_profit):
    trade = await account.create_market_buy_order(asset, volume, stop_loss=stop_loss, take_profit=take_profit)
    print(f"Trade executed: {trade['id']}")

if __name__ == "__main__":
    # Example usage in main file after strategy signals indicate a trade
    pass

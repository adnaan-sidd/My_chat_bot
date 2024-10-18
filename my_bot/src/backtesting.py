import pandas as pd
import matplotlib.pyplot as plt
from .strategies import TradingStrategies

class Backtester:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def run_backtest(self):
        signals = self.strategy.moving_average_strategy(self.data)
        portfolio = pd.DataFrame(index=signals.index)
        portfolio['positions'] = signals['positions']
        portfolio['price'] = signals['price']
        portfolio['holdings'] = portfolio['positions'] * portfolio['price']
        return portfolio

    def plot_performance(self, portfolio):
        plt.figure(figsize=(10,6))
        plt.plot(portfolio['holdings'], label='Portfolio Holdings')
        plt.title('Backtesting Performance')
        plt.legend()
        plt.show()

# Usage
if __name__ == "__main__":
    data = pd.read_csv('data/historical_data.csv')
    strategy = TradingStrategies()
    backtester = Backtester(strategy, data)
    portfolio = backtester.run_backtest()
    backtester.plot_performance(portfolio)

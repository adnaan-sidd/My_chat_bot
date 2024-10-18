import pandas as pd
import numpy as np

class TradingStrategies:
    def moving_average_strategy(self, data, short_window=40, long_window=100):
        signals = pd.DataFrame(index=data.index)
        signals['price'] = data['price']
        
        signals['short_mavg'] = data['price'].rolling(window=short_window).mean()
        signals['long_mavg'] = data['price'].rolling(window=long_window).mean()
        
        signals['signal'] = 0.0
        signals['signal'][short_window:] = np.where(
            signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0
        )
        signals['positions'] = signals['signal'].diff()
        
        return signals

if __name__ == "__main__":
    data = pd.DataFrame({'price': [1.17, 1.18, 1.19, 1.18, 1.20, 1.22, 1.19, 1.21]})
    strategy = TradingStrategies()
    signals = strategy.moving_average_strategy(data)
    print(signals)

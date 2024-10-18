import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def clean_and_normalize(self, data):
        # Assume data is a dictionary of asset prices
        df = pd.DataFrame(data, index=[0])
        
        # Normalize the price data using StandardScaler
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(df)
        
        normalized_df = pd.DataFrame(scaled_data, columns=df.columns)
        return normalized_df

if __name__ == "__main__":
    sample_data = {
        'EURUSD': 1.1735,
        'GBPUSD': 1.3825,
        'JPYUSD': 110.25,
        'XAUUSD': 1750.10
    }

    processor = DataProcessor()
    normalized_data = processor.clean_and_normalize(sample_data)
    print(normalized_data)

import yfinance as yf
import pandas as pd

def get_aapl_data():
    """
    Downloads historical stock data for AAPL (Apple Inc.) using yfinance.
    
    Returns:
        pd.DataFrame: Historical data including Open, High, Low, Close, Adj Close, Volume.
    """
    # Download data for the last 1 year
    data = yf.download('AAPL', period='1y')
    return data

# Example usage
if __name__ == "__main__":
    aapl_data = get_aapl_data()
    print(aapl_data.head())  # Print the first few rows
    print(f"\nData shape: {aapl_data.shape}")
    print(f"Columns: {list(aapl_data.columns)}")
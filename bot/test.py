import yfinance as yf
import pandas as pd

def get_goog_data():
    """
    Downloads historical stock data for GOOG (Google/Alphabet Inc.) using yfinance.
    
    Returns:
        pd.DataFrame: Historical data including Open, High, Low, Close, Adj Close, Volume.
    """
    # Download data for the last 1 year
    data = yf.download('GOOG', period='1y')
    return data

# Example usage
if __name__ == "__main__":
    goog_data = get_goog_data()
    print(goog_data.head())  # Print the first few rows
    print(f"\nData shape: {goog_data.shape}")
    print(f"Columns: {list(goog_data.columns)}")
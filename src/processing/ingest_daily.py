import pandas as pd
from datetime import datetime
from src.api_clients.mock_price_feed import generate_mock_prices
from src.processing.load_openflights import load_routes_data

def batch_ingest(output_path='data/daily_prices.csv', routes_path='data/routes.csv'):
    """Simulate a daily batch ingestion that fetches mock price data for all routes.

    Args:
        output_path (str): Path to save the generated price data CSV.
        routes_path (str): Path to the input airline route data CSV.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    routes_df = load_routes_data(routes_path)
    prices_df = generate_mock_prices(routes_df, today)
    prices_df.to_csv(output_path, index=False)
    print(f"Ingested {len(prices_df)} rows for {today}.")

if __name__ == '__main__':
    batch_ingest()

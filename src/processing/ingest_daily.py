import pandas as pd
from datetime import datetime
from src.api_clients.mock_price_feed import generate_mock_prices
from src.processing.load_openflights import load_routes_data

def batch_ingest(output_path='data/daily_prices.csv', routes_path='data/routes.csv'):
    today = datetime.today().strftime('%Y-%m-%d')
    routes_df = load_routes_data(routes_path)
    prices_df = generate_mock_prices(routes_df, today)
    prices_df.to_csv(output_path, index=False)
    print(f"Ingested {len(prices_df)} rows for {today}.")

if __name__ == '__main__':
    batch_ingest()

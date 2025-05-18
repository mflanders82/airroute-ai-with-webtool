import pandas as pd
import random

def generate_mock_prices(routes_df, date):
    """Simulate fetching price data for airline routes on a specific date.

    Args:
        routes_df (pd.DataFrame): Airline route data (must include 'source_airport', 'destination_airport', and 'airline').
        date (str): Date string in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Simulated pricing data including route, price, and days until departure.
    """
    mock_data = []
    for _, row in routes_df.iterrows():
        price = random.randint(100, 1200)
        mock_data.append({
            'origin': row['source_airport'],
            'destination': row['destination_airport'],
            'airline': row['airline'],
            'date': date,
            'price': price,
            'days_until_departure': (pd.to_datetime(date) - pd.Timestamp.today()).days
        })
    return pd.DataFrame(mock_data)

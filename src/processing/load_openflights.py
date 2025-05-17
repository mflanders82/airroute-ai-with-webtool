import pandas as pd

def load_routes_data(filepath):
    """Load the OpenFlights routes dataset."""
    df = pd.read_csv(filepath)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

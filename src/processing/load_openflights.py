import pandas as pd

def load_routes_data(filepath):
    """Load and clean airline route data from a CSV file.

    Args:
        filepath (str): Path to the routes CSV file.

    Returns:
        pd.DataFrame: Cleaned route data with standardized column names.
    """
>>>>>>> fae6b4a (changes to repo)
    df = pd.read_csv(filepath)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

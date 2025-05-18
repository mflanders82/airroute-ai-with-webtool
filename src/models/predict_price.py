import pandas as pd
from sklearn.linear_model import LinearRegression

def train_price_model(df):
    """Train a linear regression model to predict flight prices.

    Args:
        df (pd.DataFrame): Dataset with at least 'price' and 'days_until_departure' columns.

    Returns:
        LinearRegression: Trained price prediction model.
    """
    df = df.dropna(subset=['price', 'days_until_departure'])
    X = df[['days_until_departure']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_price(model, days_until_departure):
    """Predict the price of a flight given days until departure.

    Args:
        model (LinearRegression): Trained model.
        days_until_departure (int): Days before the flight.

    Returns:
        float: Predicted flight price.
    """
    return model.predict([[days_until_departure]])[0]

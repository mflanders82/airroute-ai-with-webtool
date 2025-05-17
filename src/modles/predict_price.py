import pandas as pd
from sklearn.linear_model import LinearRegression

def train_price_model(df):
    """Train a simple linear regression model for price prediction."""
    df = df.dropna(subset=['price', 'days_until_departure'])
    X = df[['days_until_departure']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_price(model, days_until_departure):
    return model.predict([[days_until_departure]])[0]

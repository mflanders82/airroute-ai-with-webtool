import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from src.processing.load_openflights import load_routes_data
from src.api_clients.mock_price_feed import generate_mock_prices
from src.models.predict_price import train_price_model, predict_price

# Set paths
DATA_PATH = 'data/routes.csv'

# Load and preprocess route data
@st.cache_data
def get_routes():
    df = load_routes_data(DATA_PATH)
    df = df.dropna(subset=['source_airport', 'destination_airport'])
    return df

# UI layout
st.title("✈️ AirRoute AI - Flight Price Predictor")

routes_df = get_routes()
airports = sorted(set(routes_df['source_airport']) | set(routes_df['destination_airport']))

col1, col2 = st.columns(2)
with col1:
    origin = st.selectbox("Origin Airport", airports)
with col2:
    destination = st.selectbox("Destination Airport", airports)

days_out = st.slider("Days Until Departure", min_value=1, max_value=180, value=30)
selected_date = (datetime.today() + timedelta(days=days_out)).strftime('%Y-%m-%d')

if st.button("Search Flights"):
    # Filter routes between origin and destination
    matched_routes = routes_df[
        (routes_df['source_airport'] == origin) & 
        (routes_df['destination_airport'] == destination)
    ]

    if matched_routes.empty:
        st.warning("No routes found for this origin-destination pair.")
    else:
        st.success(f"Found {len(matched_routes)} route(s). Generating price predictions...")
        prices_df = generate_mock_prices(matched_routes, selected_date)
        model = train_price_model(prices_df)
        prices_df['predicted_price'] = prices_df['days_until_departure'].apply(lambda x: predict_price(model, x))
        st.dataframe(prices_df[['airline', 'origin', 'destination', 'date', 'price', 'predicted_price']])


# learn-ai
=======
# ✈️ AirRoute AI

AirRoute AI is a lightweight personal project to simulate and predict the best airline routes globally, using price data, route information, and load factor estimation. It supports both local execution and cloud-based notebooks (like Kaggle).

## 📦 Project Structure

```
airroute-ai/
├── data/                 # Raw datasets (e.g. OpenFlights routes)
├── notebooks/            # Jupyter/Kaggle notebooks for exploration
├── src/                  # Source code
│   ├── api_clients/      # Mock or real API integration
│   ├── models/           # Prediction model logic
│   ├── processing/       # Data loading and transformation
│   └── utils/            # Optional helpers
├── tests/                # Test cases (to be added)
├── config/               # Configs or secrets (optional)
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

## 🚀 How to Use

### 1. Prepare Environment
```bash
pip install -r requirements.txt
```

### 2. Add Data
- Download `routes.csv` from [OpenFlights on Kaggle](https://www.kaggle.com/datasets/open-flights/airline-route-database)
- Place it in `data/routes.csv`

### 3. Run Ingestion
```bash
python src/processing/ingest_daily.py
```

### 4. Open Notebook
- Open `notebooks/explore_openflights.ipynb` in Jupyter or Kaggle
- It will auto-detect the environment and work accordingly

## 🧠 Features

- Simulates pricing using mock API
- Loads global airline routes
- Trains a simple predictive model using `scikit-learn`
- Future support for real APIs and better load factor proxies

---
Created for experimentation and learning.
>>>>>>> fae6b4a (changes to repo)

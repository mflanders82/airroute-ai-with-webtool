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

## 🚀 Local Environment Setup & Usage

### 1. Prepare Python Environment

Requires Python 3.8+

(Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Main dependencies:
- requests
- pandas
- numpy
- scikit-learn
- matplotlib
- openpyxl
- streamlit

### 3. Add Data

Download `routes.csv` from OpenFlights on Kaggle and place it at `data/routes.csv`.

### 4. Ingest Data

Run the ingestion script to generate mock pricing data:

```bash
python src/processing/ingest_daily.py
```

This will create `data/daily_prices.csv`.

### 5. Run the Application

#### A. Run the Streamlit Web App

Launch the interactive web tool:

```bash
streamlit run app.py
```

This opens the app in your browser for flight price exploration.

#### B. Explore in Jupyter Notebook

Start Jupyter:

```bash
jupyter notebook
```

Open `notebooks/explore_openflights.ipynb`. The notebook will auto-detect the environment.

### 6. (Optional) Configuration

For mock/demo mode, no environment variables are needed. If you plan to use real APIs or sensitive data, create a `.env` file or add configs under `config/` as required.

## 🔗 Using on Kaggle & Jupyter Notebooks

### A. Running on Kaggle

#### Upload Code and Data:

Upload your `src/`, `notebooks/`, and `requirements.txt` to a new Kaggle Notebook. Add the OpenFlights airline-route-database dataset as a Dataset in the notebook settings.

#### Adjust Data Paths:

The notebook `notebooks/explore_openflights.ipynb` will detect if running on Kaggle and set correct paths automatically.

#### Install Additional Packages (if needed):

If any required package is missing, install it with:

```python
!pip install scikit-learn matplotlib openpyxl
```

#### Run Cells:

Execute notebook cells step by step to explore data, generate mock prices, and train models.

### B. Using Jupyter Locally

#### Start Jupyter:

```bash
jupyter notebook
```

#### Open the Notebook:

Navigate to `notebooks/explore_openflights.ipynb`.

#### Check Data Location:

Ensure `data/routes.csv` exists as described above. The notebook will auto-detect and use the local data path.

#### Run Notebook:

Execute cells to explore airline routes, simulate prices, and train predictive models.

## 🧠 Features

- Simulates pricing using a mock API
- Loads global airline routes
- Trains a simple predictive model using scikit-learn
- Future support for real APIs and better load factor proxies

## ❓ Troubleshooting

- If you see import errors, ensure you're in the project root and your virtual environment is active.
- If `streamlit` or `jupyter` are not found, double-check that installation succeeded (`pip install -r requirements.txt`).
- For Windows, use `venv\Scripts\activate` to activate your virtual environment.

Created for experimentation and learning.


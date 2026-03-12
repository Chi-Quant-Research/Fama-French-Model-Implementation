import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import os
import zipfile
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Create folders
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# -----------------------------
# Download stock data
# -----------------------------

ticker = "AAPL"

data = yf.download(ticker, start="2018-01-01", auto_adjust=True)

data["Return"] = data["Close"].pct_change()

# -----------------------------
# Download Fama-French factors
# -----------------------------

url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip"

response = requests.get(url)

zip_file = zipfile.ZipFile(BytesIO(response.content))

ff = pd.read_csv(zip_file.open(zip_file.namelist()[0]), skiprows=4)

# Clean dataset
ff = ff.rename(columns={"Mkt-RF":"Mkt_RF"})
ff = ff.dropna()

ff = ff.iloc[:-1]

ff["Date"] = pd.to_datetime(ff["Unnamed: 0"], format="%Y%m%d")

ff = ff.set_index("Date")

ff = ff[["Mkt_RF","SMB","HML","RF"]]

ff = ff / 100

# -----------------------------
# Prepare dataset
# -----------------------------

dataset = pd.DataFrame()

dataset["Return"] = data["Return"]

dataset = dataset.join(ff, how="inner")

dataset["Excess_Return"] = dataset["Return"] - dataset["RF"]

dataset = dataset.dropna()

print("Number of observations:", len(dataset))

# -----------------------------
# Regression
# -----------------------------

X = dataset[["Mkt_RF","SMB","HML"]]
y = dataset["Excess_Return"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())

# -----------------------------
# Save dataset
# -----------------------------

dataset.to_csv("data/factor_dataset.csv")

# -----------------------------
# Save regression results
# -----------------------------

with open("results/fama_french_regression.txt","w") as f:
    f.write(model.summary().as_text())

# -----------------------------
# Plot Factor Exposure
# -----------------------------

betas = model.params[1:]  # exclude intercept

plt.figure(figsize=(8,5))

betas.plot(kind="bar")

plt.title("Fama-French Factor Loadings")

plt.ylabel("Coefficient")

plt.xlabel("Factor")

plt.tight_layout()

plt.savefig("results/factor_exposure.png")

plt.show()
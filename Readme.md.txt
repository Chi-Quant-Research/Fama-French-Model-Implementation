# Fama-French Factor Model Implementation

## Overview

Asset pricing research has long attempted to explain differences in stock returns using systematic risk factors. One of the most influential models in empirical finance is the Fama-French factor model, which extends the traditional CAPM by introducing additional risk factors related to firm size and value characteristics.

This project implements the Fama-French Three-Factor Model using historical stock data and publicly available factor datasets. The objective is to demonstrate how factor models can be estimated using Python and applied in empirical financial analysis.

The project illustrates the following workflow:

* Financial data acquisition
* Factor model construction
* Regression-based asset pricing estimation
* Empirical interpretation of factor exposures

This repository is part of a financial analytics portfolio showcasing quantitative approaches in asset pricing and financial econometrics.

---

# Background

The traditional Capital Asset Pricing Model (CAPM) explains expected returns using market risk alone.

The Fama-French model extends this framework by introducing two additional factors:

1. **SMB (Small Minus Big)**
   Captures the return difference between small-cap and large-cap firms.

2. **HML (High Minus Low)**
   Captures the return difference between value stocks and growth stocks.

The model can be written as:

Ri - Rf = α + β₁(Rm - Rf) + β₂SMB + β₃HML + ε

Where:

* Ri = asset return
* Rf = risk-free rate
* Rm = market return
* SMB = size factor
* HML = value factor

This model is widely used in empirical asset pricing research.

---

# Dataset

Two data sources are used:

**1. Stock price data**

Downloaded from Yahoo Finance using the `yfinance` API.

Example asset:

* Apple (AAPL)

**2. Fama-French factors**

Factor data is obtained from the data library maintained by Kenneth R. French Data Library.

Factors used:

* Market risk premium (Mkt-RF)
* SMB (size factor)
* HML (value factor)
* Risk-free rate

---

# Methodology

## 1. Data Collection

Stock price data is downloaded using the `yfinance` API and converted into daily returns.

Fama-French factor data is loaded from the public data library.

---

## 2. Data Preparation

The following steps are performed:

* Convert price data to returns
* Align stock returns with factor data
* Calculate excess returns over the risk-free rate

This ensures the regression model is correctly specified.

---

## 3. Factor Model Estimation

The Fama-French regression is estimated using **ordinary least squares (OLS)**.

The model estimates the following parameters:

* Alpha (abnormal return)
* Market beta
* Size exposure
* Value exposure

These coefficients represent the sensitivity of the asset to systematic risk factors.

---

# Example Output

Example regression output:

Alpha: 0.0003
Market Beta: 1.12
SMB Loading: -0.25
HML Loading: -0.41

Interpretation:

* The stock has strong exposure to the overall market.
* Negative SMB suggests characteristics closer to large-cap firms.
* Negative HML indicates a growth-oriented profile.

---

# Output

Dataset

data/factor_dataset.csv

Regression results

results/fama_french_regression.txt


## Factor Exposure

The estimated factor loadings are illustrated below.

![Factor Exposure](results_factor_exposure.png)

---

# Project Structure

```
fama-french-factor-model
│
├── data
│
├── results
│
├── fama_french_model.py
├── requirements.txt
└── README.md
```

---

# How to Run

Clone the repository

```
git clone https://github.com/yourusername/fama-french-factor-model.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the script

```
python fama_french_model.py
```

The script will:

* Download stock price data
* Load Fama-French factor data
* Estimate the factor model
* Save regression results

---

# Key Takeaways

This project demonstrates how factor models can be implemented in Python to study asset pricing behavior.

Key insights include:

* Stock returns can be decomposed into systematic risk factors
* Factor models provide a richer explanation than CAPM alone
* Empirical finance methods rely heavily on regression analysis and data alignment

The framework presented here can be extended to include:

* Fama-French Five-Factor Model
* Momentum factor models
* Cross-sectional asset pricing tests

---

# Technologies Used

Python libraries:

* pandas
* numpy
* statsmodels
* yfinance

---

# Disclaimer

This project is intended for educational and research purposes only.
It does not constitute financial advice or investment recommendations.

# Linear-regression
A simple Python project that predicts car prices based on mileage using linear regression. It includes a training script (train.py) that learns from a CSV dataset, and a prediction script (predict.py) that estimates price using the trained model saved in thetas.json.

# 🚗 Car Price Predictor using Linear Regression

This project implements a simple linear regression model to estimate car prices based on mileage.

## 📌 Description

- `train.py`: Trains the model using gradient descent on `data.csv`, and saves the learned values (`theta0`, `theta1`) to a `thetas.json` file.
- `predict.py`: Prompts the user for a mileage and predicts the car price using the saved model.

## 🧠 Formula

The model is based on the linear equation: price = θ0 + θ1 * mileage

## 🛠 Technologies

- Python 3
- GitHub Codespaces (no local setup needed)
- CSV file as the dataset

## 📂 Files

- `train.py` – model training logic
- `predict.py` – price prediction based on input mileage
- `data.csv` – dataset file (mileage, price)
- `thetas.json` – stores the trained model parameters

## ▶️ How to Run

Inside GitHub Codespaces or any Python environment:

```bash
# To train the model
python3 train.py

# To predict the price
python3 predict.py
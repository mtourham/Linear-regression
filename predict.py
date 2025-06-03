import json

# Load trained parameters
with open('thetas.json', 'r') as file:
    thetas = json.load(file)

theta0 = thetas['theta0']
theta1 = thetas['theta1']

def predict(km):
    return theta0 + theta1 * km

# Take user input
try:
    km_input = float(input("Enter kilometers: "))
    predicted_price = predict(km_input)
    print(f"Predicted price: {predicted_price:.2f} €")
except ValueError:
    print("Invalid input. Please enter a valid number.")

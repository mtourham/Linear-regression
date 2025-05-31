import json

with open('thetas.json', 'r') as file:
    thetas = json.load(file)

# Access the values
theta0 = thetas['theta0']
theta1 = thetas['theta1']

print(theta0, theta1, thetas)
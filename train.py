import json
import csv

x = []
y = []

with open('thetas.json', 'r') as file:
    thetas = json.load(file)

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(float(row['km']))
        y.append(float(row['price']))

# Access the values
theta0 = thetas['theta0']
theta1 = thetas['theta1']

learing_rate = 0.1

iterations = 1000

sum_error0 = 0
sum_error1 = 0

predictions = []

for i,kms in enumerate(x):
    predictions.append(theta0 + (theta1 * kms)
    if predictions[i] != y[i]:
        
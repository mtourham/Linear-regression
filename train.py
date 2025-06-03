import json
import csv

x = []
y = []

# Load dataset
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(float(row['km']))
        y.append(float(row['price']))

# Normalize x and y
x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)

x_norm = [(xi - x_min) / (x_max - x_min) for xi in x]
y_norm = [(yi - y_min) / (y_max - y_min) for yi in y]

theta0 = 0
theta1 = 0

learning_rate = 0.01
iterations = 20000
m = len(x)

# Gradient Descent
for i in range(iterations):
    sum_error0 = 0
    sum_error1 = 0

    for j in range(m):
        prediction = theta0 + theta1 * x_norm[j]
        error = prediction - y_norm[j]
        sum_error0 += error
        sum_error1 += error * x_norm[j]

    theta0 -= learning_rate * (sum_error0 / m)
    theta1 -= learning_rate * (sum_error1 / m)

    # Optional: print MSE every 500 iterations
    if i % 500 == 0:
        mse = sum((theta0 + theta1 * x_norm[j] - y_norm[j]) ** 2 for j in range(m)) / m
        print(f"Iteration {i}: MSE (normalized) = {mse:.6f}")

# Denormalize thetas
# y = theta0 + theta1 * x
# real_y = y_norm * (y_max - y_min) + y_min
# real_x = x_norm * (x_max - x_min) + x_min
# Solve for: real_y = a + b * real_x

# Let’s substitute x_norm = (x - x_min) / (x_max - x_min)
# Then: y = theta0 + theta1 * ((x - x_min) / (x_max - x_min))

# After denormalizing:
true_theta1 = theta1 * (y_max - y_min) / (x_max - x_min)
true_theta0 = y_min + (y_max - y_min) * theta0 - true_theta1 * x_min

# Save denormalized thetas and normalization data
with open('thetas.json', 'w') as file:
    json.dump({
        'theta0': true_theta0,
        'theta1': true_theta1,
        'min_km': x_min,
        'max_km': x_max
    }, file)

print(f"Training complete.\ntheta0 = {true_theta0:.2f}, theta1 = {true_theta1:.2f}")

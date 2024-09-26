import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.ticker import FuncFormatter

# Ask the user for the size of the Galton board and the number of steps (iterations)
n = int(input("Introduce the size of the Galton Board: "))
N = int(input("Introduce the number of steps: "))

# Initialize the board with n positions, all set to 0
board = [0] * (n+1)

# Simulate the Galton board
for i in range(N):
    position = 0
    for j in range(n):
        position += random.choice([0, 1])  # Randomly add 0 or 1 to each position with probability 0.5
    board[position] += 1

# Normalize the board by dividing by the total number of balls 
board = [x/ N for x in board]

# For the plot
plt.title(f"Galton Board Simulation for n = {n:.0f} and N = {N:.0f}.")
plt.xlabel('Position')
plt.ylabel('Quantity of balls')

# Plot the results of the binomial as a bar chart
plt.bar(range(n+1), board, label = 'Binomial distribution')

# Generate a range of x values from 0 to n
x = np.linspace(0, n, N)

# Compute the normal distribution's PDF for these x values
y = norm.pdf(x, n/2, math.sqrt(n/4))

# Create the plot of the normal distribution
plt.plot(x, y, color='red', label = 'Normal distribution')

# Define a to_percent function for the y label
def to_percent(y, position):
    # Multiply by 100 and add a percent sign
    return f'{100 * y:.0f}%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

# Calculate the Mean Quatratic mean
zx = np.linspace(0, n, n+1)
zy = norm.pdf(zx, n/2, math.sqrt(n/4))
MQE = np.sum(np.square(zy-board))/2

# Calculate the mean and the variance of the generated binomial distribution
positions = np.arange(n+1)
mean = np.sum(positions * board)
variance = np.sum(board * (positions - mean)**2)

# Add text below the plot
plt.subplots_adjust(bottom=0.50)  # Increase bottom margin to 50% of the figure height
plt.figtext(0.05, 0.35, f"The mean quatratic error is {MQE:.6f}.", fontsize=12)
plt.figtext(0.05, 0.29, f"The mean of the normal distribution is {n/2:.6f}.", fontsize=11)
plt.figtext(0.05, 0.24, f"The mean of the binomial distribution is {mean:.6f}.", fontsize=11)
plt.figtext(0.05, 0.19, f"(The difference between both means is {abs(mean-n/2):.6f}.)", fontsize=11)
plt.figtext(0.05, 0.14, f"The variance of the normal distribution is {n/4:.6f}.", fontsize=11)
plt.figtext(0.05, 0.09, f"The variance of the binomial distribution is {variance:.6f}.", fontsize=11)
plt.figtext(0.05, 0.04, f"(The difference between both variances is {abs(n/4-variance):.6f}.)", fontsize=11)

plt.legend()
plt.show()
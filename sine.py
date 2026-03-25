import numpy as np
import matplotlib.pyplot as plt

# Generate evenly spaced X values
X = np.linspace(0, 10 * np.pi, 1000)

# Apply sine function
Y = np.sin(X)

# Create figure and axis
fig, ax = plt.subplots()

# Plot the sine wave
ax.plot(X, Y)

# Add labels and title
ax.set_title("Sine Wave (5 Cycles)")
ax.set_xlabel("Angle (radians)")
ax.set_ylabel("sin(X)")

# Optional: Add grid
ax.grid(True)

# Display the plot
plt.show()
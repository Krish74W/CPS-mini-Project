mport numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Function to compute the projectile motion
def projectile_motion(t, y, g):
    # y = [x, y, vx, vy]
    x, y_pos, vx, vy = y
    dydt = [vx, vy, 0, -g]  # dx/dt = vx, dy/dt = vy, ax = 0, ay = -g
    return dydt

# Get inputs from the user
initial_velocity = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the launch angle (degrees): "))
initial_height = float(input("Enter the initial height (m): "))
gravity = 9.81  # Acceleration due to gravity (m/s^2)

# Convert angle to radians
angle_rad = np.radians(angle)

# Initial conditions
vx = initial_velocity * np.cos(angle_rad)  # Horizontal velocity
vy = initial_velocity * np.sin(angle_rad)  # Vertical velocity
y0 = [0, initial_height, vx, vy]  # [x, y, vx, vy]

# Time span for the simulation
t_span = (0, 10)  # Simulate for 10 seconds (adjustable)
t_eval = np.linspace(0, 10, 1000)  # Time points for solution evaluation

# Solve the ODE
solution = solve_ivp(projectile_motion, t_span, y0, t_eval=t_eval, args=(gravity,))

# Extract results
x = solution.y[0]  # Horizontal position
y = solution.y[1]  # Vertical position

# Stop when the projectile hits the ground (y >= 0)
valid_indices = y >= 0
x = x[valid_indices]
y = y[valid_indices]

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Projectile Path")
plt.title("Projectile Motion Simulation")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid()
plt.legend()
plt.show()

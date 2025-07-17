import numpy as np
import matplotlib.pyplot as plt
import random


def function_generator(x, y):
    """
    Generates a scene as follows:
    3 consecetivly mountains , folowed by a valley and ended with a  tallest mountain
    --------------------------------------------------------------------------------- 
    In other words:  3 Local Max followed by a Global Min and a Global Max 
    - mountain parameters (amplitude, center, and width)
    """
    # 1st mountains (Sorted based on their height)
    A1, x1, y1, sig_1 = 18, -8, 0, 1.5  
    # 2nd mountains
    A2, x2, y2, sig_2 = 12, -4, 3, 1.5
    # 3rd mountains
    A3, x3, y3, sig_3 = 7, 0, 4, 1.5
    # Valley (inverted gaussian bell, hence we need to use negative values for A4)
    A4, x4, y4, sig_4 = -8, 4, -2, 3
    # Tallest mountain (This is our desired max)
    A5, x5, y5, sig_5 = 24, 7, 2, 1.5

    # Now we need to create gaussian functions for each mountain and valley
    f1 = A1 * np.exp(-((x - x1)**2 + (y - y1)**2) / (2 * sig_1**2))
    f2 = A2 * np.exp(-((x - x2)**2 + (y - y2)**2) / (2 * sig_2**2))
    f3 = A3 * np.exp(-((x - x3)**2 + (y - y3)**2) / (2 * sig_3**2))
    f4 = A4 * np.exp(-((x - x4)**2 + (y - y4)**2) / (2 * sig_4**2))  
    f5 = A5 * np.exp(-((x - x5)**2 + (y - y5)**2) / (2 * sig_5**2))

    # Put them all together and generate a 3D space
    z = f1 + f2 + f3 + f4 + f5 
    return z


def generate_neighbors(x, y, step_size, num_neighbors=10):
    """This function generates random neighbours at each step"""
    neighbors = []
    # for the number of neighbours specified
    for _ in range(num_neighbors):
        # generate random step coordinates corespounding to the neighbouring state
        dx = random.uniform(-step_size, step_size) 
        dy = random.uniform(-step_size, step_size)
        neighbors.append((x + dx, y + dy))
    return neighbors


def best_neighbor(x, y, step_size):
    """This is helper function that deployes the greedy nature of Hill climbing"""
    # generate the neighbours and initially pick the first input as the best neighbout but ...
    neighbors = generate_neighbors(x, y, step_size)
    best_x, best_y = x, y
    best_value = function_generator(x, y)

    # here is the but:
    # for each possible neighbour acquired from the genrated 3D space
    for nx, ny in neighbors:
        current_value = function_generator(nx, ny)
        # if it is better than what you already have, pick it (Greedy)
        if current_value > best_value:
            best_x, best_y = nx, ny
            best_value = current_value
    return best_x, best_y, best_value


# Hill Climbing algorithm
def hill_climbing(start, step_size, max_iterations):
    current_x, current_y = start
    current_value = function_generator(current_x, current_y)
    path = [(current_x, current_y, current_value)]
    # here is the greedy nature ...
    for _ in range(max_iterations):
        best_x, best_y, best_value = best_neighbor(current_x, current_y, step_size)

        if best_value > current_value:
            current_x, current_y, current_value = best_x, best_y, best_value
            path.append((current_x, current_y, current_value))
        else:
            break  # Stop if no better neighbor is found

    return path



# Initialize the HC and run it ---------------------------------------------------------------
start_point = (0,0)   # We could have started randomly
step_size = 0.5       # Step size for neighbors (perhaps we can call it Learning Rate!)
max_iterations = 500  # Maximum iterations (perhaps we can call it epochs)
path = hill_climbing(start_point, step_size, max_iterations)


# Viz ----------------------------------------------------------------------------------------
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = function_generator(X, Y) # This is the space we want to plot

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=0.4)

# Plot the entire Hill Climbing path
path_x, path_y, path_z = zip(*path)
ax.plot(path_x, path_y, path_z, color='cyan', marker='o', markersize=4, label="Hill Climbing Path", linestyle='-', linewidth=2)
ax.set_title("Hill Climbing")
ax.legend()
plt.show()

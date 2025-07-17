import numpy as np
import matplotlib.pyplot as plt
import random
from Function_Generator import function_generator, generate_neighbor


def simulated_annealing(start, step_size, max_iterations, initial_temp, temp_decay, temp_thresh = 1e-6):
    """
    This function deployes the Simulated Annealing Algorithm (SNA)
    An optimization algorithm that approximates the global optimum of a given function.
    """
    current_x, current_y = start
    current_value = function_generator(current_x, current_y)
    best_x, best_y, best_value = current_x, current_y, current_value

    path = [(current_x, current_y, current_value)]
    temp = initial_temp
    
    # optimization loop
    for i in range(max_iterations):
        # Generate a neighbor
        neighbor_x, neighbor_y = generate_neighbor(current_x, current_y, step_size)
        neighbor_value = function_generator(neighbor_x, neighbor_y)

        # Decide whether to accept the neighbor
        delta_e = neighbor_value - current_value
        if delta_e < 0 or random.random() < np.exp(-delta_e / temp):
            current_x, current_y, current_value = neighbor_x, neighbor_y, neighbor_value
            path.append((current_x, current_y, current_value))
            
            # Update the best solution
            if current_value < best_value:
                best_x, best_y, best_value = current_x, current_y, current_value


        # Lower the temp
        temp *= temp_decay
        if temp < temp_thresh:  
            break


    return path, (best_x, best_y, best_value)


# Init -------------------------------------------------------------------------------------------------------
start_point = (random.uniform(-5, 5), random.uniform(-5, 5))
step_size = 0.3
max_iterations = 1000
initial_temp = 10
temp_decay = 0.90

path, best_solution = simulated_annealing(start_point, step_size, max_iterations, initial_temp, temp_decay)


# Visualization
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = function_generator(X, Y)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=0.2)


# Plot the path of Simulated Annealing
path_x, path_y, path_z = zip(*path)
ax.plot(path_x, path_y, path_z, 
        color='red', marker='o', markersize=2, 
        label="Simulated Annealing Path", linestyle='--', linewidth=1)


# Annotate the last step
best_x, best_y, best_value = best_solution
ax.scatter(best_x, best_y, best_value, color='black', label='Best Solution')

ax.set_title("Simulated Annealing")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.show()

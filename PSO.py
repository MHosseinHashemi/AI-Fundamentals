import numpy as np
import matplotlib.pyplot as plt
import random
from Function_Generator import function_generator


def particle_swarm_optimization(function_generator, bounds, num_particles, max_epochs):
    """
    Particle Swarm Optimization algorithm.

    Parameters:
    - function_generator: The function to optimize.
    - bounds: Tuple specifying the search space bounds [(x_min, x_max), (y_min, y_max)].
    - num_particles: Number of particles in the swarm.
    - max_epochs: Maximum number of epochs to perform.
    """
    x_min, x_max = bounds[0]
    y_min, y_max = bounds[1]


    # Initialize particle and velocities randomly within the range --------------------------------------------
    p = np.array([[random.uniform(x_min, x_max), random.uniform(y_min, y_max)] for _ in range(num_particles)])
    v = np.random.uniform(-1, 1, (num_particles, 2))

    # Initialize p_best positions and their corresponding fitness values
    p_best_pos = p.copy()
    p_best_fitval = np.array([function_generator(x, y) for x, y in p])

    # Determine the g_best based on initial positions
    g_best_pos = p_best_pos[np.argmax(p_best_fitval)]
    g_best_fitval = max(p_best_fitval)

    # Hyperparameters for PSO
    inertia_weight = 0.7       # Balances exploration and exploitation
    cognitive_component = 1.5  # Particle's tendency to return to its best-known position
    social_component = 1.5     # Particle's tendency to follow the swarm's best-known position

    # Track paths of particles for visualization
    paths = [[] for index in range(num_particles)]

    # Setup 3D plot and a landscape for future visualization
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x, y)
    Z = function_generator(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Optimization loop
    for epoch in range(max_epochs):
        for i in range(num_particles):
            # Update each particle's velocity 
            r1, r2 = random.random(), random.random()
            v[i] = (
                inertia_weight * v[i] +
                cognitive_component * r1 * (p_best_pos[i] - p[i]) +
                social_component * r2 * (g_best_pos - p[i])
            )

            # Update particle position and ensure it stays within bounds
            p[i] += v[i]
            p[i][0] = np.clip(p[i][0], x_min, x_max)
            p[i][1] = np.clip(p[i][1], y_min, y_max)

            # Evaluate fitness of the new position
            fitness_value = function_generator(p[i][0], p[i][1])


            # Update personal best if the new fitness is better
            if fitness_value > p_best_fitval[i]:
                p_best_pos[i] = p[i]
                p_best_fitval[i] = fitness_value

            # Update global best if the new fitness is better
            if fitness_value > g_best_fitval:
                g_best_pos = p[i]
                g_best_fitval = fitness_value
            # Record particle path for visualization
            paths[i].append(p[i].copy())


        # Update the 3D plot with current particle positions and paths
        ax.cla()
        ax.plot_surface(X, Y, Z, cmap='inferno', alpha=0.3)
        for path in paths:
            path_array = np.array(path)
            if len(path_array) > 1:
                ax.plot(path_array[:, 0], path_array[:, 1],
                        function_generator(path_array[:, 0], path_array[:, 1]),
                        linestyle='--', linewidth=1, alpha=0.5)
        
        ax.scatter(g_best_pos[0], g_best_pos[1], g_best_fitval,
                   color='Blue', marker='o', s=20, label="Best")
        ax.set_title(f"Epochs {epoch + 1}")
        ax.legend()
        # Pause to simulate real-time updates
        plt.pause(0.5)  

    plt.show()
    return g_best_pos, g_best_fitval, paths


# Initialization
bounds = [(-10, 10), (-10, 10)]  # Search space bounds
num_particles = 20               # Number of particles in the swarm
max_epochs = 30                     


# Test run
best_position, best_value, paths = particle_swarm_optimization(function_generator, bounds, num_particles, max_epochs)
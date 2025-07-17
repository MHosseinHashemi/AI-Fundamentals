import numpy as np
import random

def function_generator(x, y):
    """This function generates any given space"""
    # # ------------------------------------- Ackley function ----------------------------------------------
    # # Source: "https://www.sfu.ca/~ssurjano/ackley.html"
    # # """
    # a = 20
    # b = 0.2
    # c = 2 * np.pi
    # var_1 = -a * np.exp(-b * np.sqrt(0.5 * (x**2 + y**2)))
    # var_2 = -np.exp(0.5 * (np.cos(c * x) + np.cos(c * y)))
    # z = var_1 + var_2 + a + np.exp(1)
    
    # return z
 
    # ------------------------- A Custom Plate with Custom Gaussian hills --------------------------------
    ##  
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


def generate_neighbor(x, y, step_size):
    """This function generates random neighbours at each step"""
    dx = random.uniform(-step_size, step_size)
    dy = random.uniform(-step_size, step_size)
    return x + dx, y + dy
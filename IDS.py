from DLS import dls  

def ids(graph, root, goal, max_depth):
    """
    Iterative Deepening Search (IDS)
    Calls DLS iteratively with increasing depth limits.

    """
    for depth in range(max_depth):
        # Call the `dls` module with the current depth
        path = dls(graph, root, goal, depth, flag=True)
        if path:  # If DLS finds a solution, return it
            print(f"IDS found a path in depth {depth}\n")
            return path
    
    print(" IDS could not find a path ...\n")
    return []  # If god forbidden you could nt find a path...... just tell us
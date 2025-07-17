# DLS: Depth Limmited Search

def dls(graph, root, goal, limit, flag = False):
    """This function simulates the Depth Limmited Search Algorithm
    graph: input graph 
    root: starting node
    goal: destination
    limit: maximum explorable depth
    flag: switch between DLS and IDS
    """
    open_list = [(root, 0)]  # Here frontier(open_list) maintains nodes to be explored along with their depths
    closed_list = []
    # Loop through all the nodes until the frontier is empty
    while open_list:
        # Same as DFS here we honor the newbies (LIFO)
        current_node, current_depth = open_list.pop()
        # Goal Checking (Same as DFS)
        if current_node == goal:
            closed_list.append(current_node)
            return closed_list
        
        # Here is the minor change:
        if current_depth < limit:
            # If we still had depths to explore
            if current_node not in closed_list:
                # and If the nodes observed in the frontier are all newbies
                closed_list.append(current_node)
                # then add their neibours (childs) and their corresponding depths to the frontier
                for child, _ in graph[current_node]:
                    open_list.append((child, current_depth + 1))

    
    return []
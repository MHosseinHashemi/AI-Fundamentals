# UCS: Uniform Cost Search

def ucs(graph, root, goal):
    open_list = [(root, 0)]  # We should keep track of each node but for now the root costs zero
    closed_list = {}

    while open_list:
        # Sort open_list by cost (smallest cost first)
        open_list.sort(key=lambda z: z[1])
        # and pick the lowest cost node to expand
        current_node, current_cost = open_list.pop(0)
        # Keep track of goal node we aim to reach the goal with lowe st cost
        if current_node == goal:
            closed_list[current_node] = current_cost
            break

        # Same as BFS we need to check all the nodes (until we reach the goal and ofcourse with lowest cost)    
        if current_node not in closed_list:
            closed_list[current_node] = current_cost
            # then expand all the nodes and append their childs to the frontier (open-list)
            for child, cost in graph[current_node]:
                if child not in closed_list:
                    open_list.append((child, current_cost + cost))

    return list(closed_list.keys())
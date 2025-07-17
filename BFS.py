# BFS : Breadth First Search

def bfs(graph, root, goal):
    open_list = [root] # Begin with the root node
    closed_list = []

# Nearly all of the conditions on BFS are identical to DFS expect:
    while open_list:
        # Here we need to serve the elders first (FIFO)
        current_node = open_list.pop(0)
        
        # Is it a goal?
        if current_node == goal:
            closed_list.append(current_node)
            # print("Yay! we reached the goal!")
            # print(closed_list)
            break

        # Same as DFS (Checking if the node have already been checked or not?)
        if current_node not in closed_list:
            closed_list.append(current_node)
            # For each child and their correspounding childs append a new instance to the Frontier (open_list)
            for child, _ in graph[current_node]:
                if child not in closed_list and child not in open_list:
                    open_list.append(child)

    return closed_list
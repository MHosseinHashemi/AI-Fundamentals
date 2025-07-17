# A* search algorithm
def a_star(graph, root, h_root, goal):
    open_list = [(root, 0, 0, None)]  # Node, g, h, parent_node
    closed_list = {}

    while open_list:
        # Select the node with the lowest f value from the open list
        open_list.sort(key=lambda z: z[1]+ z[2])
        current_node, g, h, parent = open_list.pop(0)
        closed_list[current_node] = (g, h, parent)

        # If the current node is the goal node
        # if current_node == goal:
        #     # Move the current node to the closed list
        #     closed_list[current_node] = (g,h)
        #     print("A* found a path\n")
        #     print(closed_list)
        #     break

        # If the current node is the goal node:
        # Back-Track to the root
        if current_node == goal:
            path =[]
            while current_node:
                # Iterativly insert parents to the start of path list 
                path.insert(0, current_node)
                current_node = closed_list[current_node][2] # 3rd index = Parent node 
            return path
        
            
        try: 
            childs = graph[current_node]          
        # Exception: It is possible that the node is infertile (Dead-End)
        except KeyError:
            childs = []

        # Now Iterate over all the childerens 
        for child, g_cost, h_cost in childs:
            g_new = g + g_cost
            h_new = h_cost

            # Lastly we need to check for two things:
            # 1. if the node is visited or not
            # 2. if the node had a better explored path
            if child not in closed_list or g_new < closed_list[child][0]:
                # To make sure that child is not already in open list with a better or equal path
                if not any(child == item[0] and g_new >= item[1] for item in open_list):
                    open_list.append((child, g_new, h_new, current_node))


    print("A* could not find a path")
    return []

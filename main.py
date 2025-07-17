# ============================================================================================================
#  ===========================================   READ ME  ===================================================
# ============================================================================================================
# The folowing code, simulates BFS, DFS, UCS, DLS and IDS uninformed search algorithms on a given graph.
# And generates a visualized graph of the result per algorithm.
# -----------------------------------------------------------------------------------------------------------
# Make sure to pip install the folowing packages for a fluent runtime 
# 1 - Matplotlit
# 2 - networkx

# BR 
# S. Mohammad Hossein Hashemi
# Advanced Artificial Intelligence Course - Homework 2 
# Student ID : 14034106
# ===========================================================================================================

import BFS as BFS # BFS module
import DFS as DFS # DFS module
import UCS as UCS # UCS module
import DLS as DLS # DLS module
import IDS as IDS # IDS module
import AS as AS   # A* Module
# from Uninformed_Vis import * 
from Informed_Vis import * # Visualization Module
# Graph Initialization : (This graph could be anything but beware that if you change anything here you should modify the inputs too)
graph = {
    "Start": [("B", 2), ("C", 4)],
    "B": [("D", 3), ("E", 1)],
    "C": [("F", 5)],
    "D": [("Goal", 6)],
    "E": [("Goal", 2)],
    "F": [("Goal", 3)],
    "Goal": []
}

# This version is defined as a test case for A*
# 1st Value: Child Node
# 2nd Value: g()
# 3rd Value: h()

updated_graph = {
    "Start": [("B", 5 , 1), ("C", 4, 3)],
    "B": [("D", 3, 6), ("E", 1, 3)],
    "C": [("F", 5, 5)],
    "D": [("Goal", 6, 0)],
    "E": [("Goal", 2, 0)],
    "F": [("Goal", 3, 0)],
    "Goal": []
}


# Call each module to solve the problem
# bfs_path = BFS.bfs(graph, "Start", "Goal")
# dfs_path = DFS.dfs(graph, "Start", "Goal")
# ids_path = IDS.ids(graph, "Start", "Goal", max_depth=5)
# dls_path = DLS.dls(graph, "Start", "Goal", limit=2)
# ucs_path = UCS.ucs(graph, "Start", "Goal")
a_star_path = AS.a_star(updated_graph, "Start", 1, "Goal")

# Visualization
# visualize_graph(graph, path=bfs_path)
# visualize_graph(graph, path=dfs_path)
# visualize_graph(graph, path=ids_path)
# visualize_graph(graph, path=dls_path)
# visualize_graph(graph, path=ucs_path)
visualize_graph(updated_graph, path=a_star_path)




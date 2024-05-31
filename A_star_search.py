import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.edges[from_node][to_node]

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics

    def get_heuristic(self, node, goal):
        return self.heuristics[node][goal]

# Define the graph and heuristic function (straight-line distances to Bucharest)

romania_graph = Graph()
romania_graph.edges = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

romania_heuristics = {
    'Arad': {'Bucharest': 366},
    'Zerind': {'Bucharest': 374},
    'Oradea': {'Bucharest': 380},
    'Timisoara': {'Bucharest': 329},
    'Lugoj': {'Bucharest': 244},
    'Mehadia': {'Bucharest': 241},
    'Drobeta': {'Bucharest': 242},
    'Craiova': {'Bucharest': 160},
    'Sibiu': {'Bucharest': 253},
    'Rimnicu Vilcea': {'Bucharest': 193},
    'Fagaras': {'Bucharest': 176},
    'Pitesti': {'Bucharest': 100},
    'Bucharest': {'Bucharest': 0},
    'Giurgiu': {'Bucharest': 77},
    'Urziceni': {'Bucharest': 80},
    'Hirsova': {'Bucharest': 151},
    'Eforie': {'Bucharest': 161},
    'Vaslui': {'Bucharest': 199},
    'Iasi': {'Bucharest': 226},
    'Neamt': {'Bucharest': 234}
}

romania_graph.set_heuristics(romania_heuristics)

def a_star_search(graph, start, goal):
    # Priority queue to store the nodes to be evaluated
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Dictionary to store the cost of reaching each node
    g_costs = {start: 0}

    # Dictionary to store the path to reach each node
    came_from = {start: None}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path

        for neighbor, cost in graph.neighbors(current_node).items():
            tentative_g_cost = g_costs[current_node] + cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + graph.get_heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None

# Example usage: finding the shortest path from Arad to Bucharest
start_city = 'Arad'
goal_city = 'Bucharest'
path = a_star_search(romania_graph, start_city, goal_city)
print(f"Shortest path from {start_city} to {goal_city}: {path}")

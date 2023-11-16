def map_coloring(graph):
    colors = ["Red", "Blue", "Green"]

    def is_valid(node, color, coloring):
        for neighbor in graph[node]:
            if (neighbor in coloring) and (coloring[neighbor] == color):
                return False
        return True

    def backtrack_coloring(node, coloring):
        if node not in coloring:
            for color in colors:
                if is_valid(node, color, coloring):
                    coloring[node] = color
                    next_node = next(iter(graph.keys() - set(coloring.keys())), None)
                    if next_node is None or backtrack_coloring(next_node, coloring):
                        return True
                    del coloring[node]

    coloring = {}
    start_node = next(iter(graph.keys()))
    backtrack_coloring(start_node, coloring)
    return coloring

if __name__ == "__main__":
    # Example graph representing the adjacency of regions
    map_graph = {
        "Alabama": ["Mississippi", "Florida"],
        "Alaska": [],
        "Arizona": ["California", "Nevada"],
        "Arkansas": ["Mississippi", "Louisiana"],
        "California": ["Oregon", "Arizona"],
        "Colorado": ["Nebraska"]
        # Add more regions and their neighbors as needed
    }

    coloring_solution = map_coloring(map_graph)

    if coloring_solution:
        for region, color in coloring_solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

def water_jug_dfs(x, y, z, path, visited):
    if x == z or y == z or x + y == z:
        print("Solution found:", path)
        return True

    if (x, y) in visited:
        return False

    visited.add((x, y))

    # All possible operations on jugs
    operations = [
        ("Fill jug 1", x, y, x, y),
        ("Fill jug 2", x, y, x, y),
        ("Empty jug 1", x, y, 0, y),
        ("Empty jug 2", x, y, x, 0),
        ("Pour jug 2 into jug 1", x, y, min(x + y, x), max(0, x + y - x)),
        ("Pour jug 1 into jug 2", x, y, max(0, x + y - y), min(x + y, y))
    ]

    for operation in operations:
        action, next_x, next_y, new_x, new_y = operation
        if water_jug_dfs(new_x, new_y, z, path + [action], visited):
            return True

    return False
x_capacity = 3 
y_capacity = 1
desired_quantity = 2

visited_set = set()
initial_path = []

if not water_jug_dfs(0, 0, desired_quantity, initial_path, visited_set):
    print("No solution found.")

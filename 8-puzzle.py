from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j
def generate_moves(puzzle):
    moves = []
    row, col = find_blank(puzzle)
    if row > 0:
        moves.append((-1, 0))  
    if row < 2:
        moves.append((1, 0))
    if col > 0:
        moves.append((0, -1))
    if col < 2:
        moves.append((0, 1)) 
    return moves
def move_puzzle(puzzle, move):
    new_puzzle = [row[:] for row in puzzle]
    row, col = find_blank(puzzle)
    d_row, d_col = move
    new_puzzle[row][col], new_puzzle[row + d_row][col + d_col] = new_puzzle[row + d_row][col + d_col], new_puzzle[row][col]
    return new_puzzle
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                r, c = divmod(puzzle[i][j] - 1, 3)
                distance += abs(i - r) + abs(j - c)
    return distance
def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    visited = {tuple(map(tuple, initial_state))}
    while not frontier.empty():
        priority, current_state = frontier.get()
        if current_state == goal_state:
            return current_state
        for move in generate_moves(current_state):
            new_state = move_puzzle(current_state, move)
            if tuple(map(tuple, new_state)) not in visited:
                visited.add(tuple(map(tuple, new_state)))
                priority = manhattan_distance(new_state)
                frontier.put((priority, new_state))
    
    return None
initial_puzzle = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solution = solve_puzzle(initial_puzzle)

if solution:
    print("Solution found!")
    for row in solution:
        print(row)
else:
    print("No solution found.")

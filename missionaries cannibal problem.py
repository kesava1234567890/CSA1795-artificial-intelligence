from collections import deque
class State:
    def __init__(self, missionaries, cannibals, boat, parent):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent
def is_valid(state):
    if state.missionaries < 0 or state.missionaries > 3 or state.cannibals < 0 or state.cannibals > 3 or (state.missionaries != 0 and state.missionaries < state.cannibals):
        return False
    return True
def print_solution(state):
    path = []
    while state:
        path.append((state.missionaries, state.cannibals, state.boat))
        state = state.parent
    path.reverse()
    for s in path:
        print(s)
def solve():
    initial_state = State(3, 3, 1, None)
    if is_valid(initial_state):
        queue = deque([initial_state])
        visited = set()
        while queue:
            current_state = queue.popleft()
            if current_state.missionaries == 0 and current_state.cannibals == 0 and current_state.boat == 0:
                print("Solution found:")
                print_solution(current_state)
                return
            for missionary in range(4):
                for cannibal in range(4):
                    if missionary + cannibal <= 2 and missionary + cannibal > 0:
                        if current_state.boat == 1:
                            new_state = State(current_state.missionaries - missionary, current_state.cannibals - cannibal, 0, current_state)
                        else:
                            new_state = State(current_state.missionaries + missionary, current_state.cannibals + cannibal, 1, current_state)
                        if is_valid(new_state) and (new_state.missionaries, new_state.cannibals, new_state.boat) not in visited:
                            queue.append(new_state)
                            visited.add((new_state.missionaries, new_state.cannibals, new_state.boat))
        print("No solution found.")
solve()

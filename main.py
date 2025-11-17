import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Heuristic function: Manhattan distance
def heuristic(state):
    d = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x, y = divmod(value-1, 3)
                d += abs(x-i) + abs(y-j)
    return d

# Find the position of the empty tile (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Move the empty tile in valid directions
def get_neighbors(state):
    zero_x, zero_y = find_zero(state)
    neighbors = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        x, y = zero_x + dx, zero_y + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row[:] for row in state]
            new_state[zero_x][zero_y], new_state[x][y] = new_state[x][y], new_state[zero_x][zero_y]
            neighbors.append(new_state)
    return neighbors

# A* algorithm
def solve(start_state):
    start_tuple = tuple(tuple(row) for row in start_state)
    goal_tuple = tuple(tuple(row) for row in goal_state)
    
    pq = [(heuristic(start_state), 0, start_state, [])]
    visited = set()
    
    while pq:
        est, cost, state, path = heapq.heappop(pq)
        state_tuple = tuple(tuple(row) for row in state)
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        if state_tuple == goal_tuple:
            return path + [state]
        
        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (cost + 1 + heuristic(neighbor), cost + 1, neighbor, path + [state]))

    return None

# Example scrambled state from the image:
start_state = [[1, 6, 5],
               [7, 3, 8],
               [0, 4, 2]]

solution = solve(start_state)
if solution:
    for step in solution:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")

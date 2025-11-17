from collections import deque

def water_jug_bfs():
    # (amount in 4-gal jug, amount in 3-gal jug)
    initial_state = (0, 0)
    goal_state = (2, 0)
    # Keep track of visited states to avoid cycles
    visited = set()
    # Each item in queue: (state, path history)
    queue = deque([(initial_state, [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Check if we have the required solution
        if a == 2:
            return path + [(a, b)]

        # Generate all possible next moves
        possible_moves = [
            ((4, b), "Fill 4-gal jug from pump"),
            ((a, 3), "Fill 3-gal jug from pump"),
            ((0, b), "Empty 4-gal jug on ground"),
            ((a, 0), "Empty 3-gal jug on ground"),
            # Pour from 4-gal to 3-gal
            ( (a - min(a, 3-b), b + min(a, 3-b)), "Pour 4-gal into 3-gal"),
            # Pour from 3-gal to 4-gal
            ( (a + min(b, 4-a), b - min(b, 4-a)), "Pour 3-gal into 4-gal"),
        ]

        for (next_a, next_b), action in possible_moves:
            if (next_a, next_b) not in visited:
                queue.append( ((next_a, next_b), path + [(a, b, action)] ))

    return None

solution = water_jug_bfs()
if solution:
    for step in solution:
        if len(step) == 3:
            print(f"{step[2]} -> State: (4-gal={step[0]}, 3-gal={step[1]})")
        else:
            print(f"Final State: (4-gal={step[0]}, 3-gal={step[1]})")
else:
    print("No solution found.")

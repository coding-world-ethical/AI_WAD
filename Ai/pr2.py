def count_clashes(board):
    board_positions = []
    n = len(board)
    for i in range(n):
        board_positions.append((board[i], i))
    clash_count = 0
    for i in range(n - 1):
        position_a = board_positions[i]
        for j in range(i + 1, n):
            position_b = board_positions[j]
            if (abs(position_a[0] - position_b[0]) == abs(position_a[1] - position_b[1])):
                clash_count += 1
            if (position_a[0] == position_b[0]):
                clash_count += 1
    return clash_count

def find_successors(current_position):
    global n, successor_positions
    for i in range(n):
        for j in range(n):
            if current_position[i] != j:
                new_position = current_position.copy()
                new_position[i] = j
                successor_positions.append(new_position)

n = int(input("Enter value of n: "))
initial_position = []
for i in range(n):
    initial_position.append(int(input(f"Row number of {i}th Queen: ")))

h = count_clashes(initial_position)
print(f"The Heuristic Value is {h}")

old_h = 99
current_position = initial_position.copy()

while old_h > h:
    successor_positions = []
    find_successors(current_position)
    min_clashes = 99
    best_position = []
    
    for position in successor_positions:
        clashes = count_clashes(position)
        if clashes < min_clashes:
            min_clashes = clashes
            best_position = position.copy()
    
    old_h = h
    h = min_clashes
    current_position = best_position.copy()
    print(current_position, h)
    
    if h == 0:
        break

if h == 0:
    print("\n\nSolution to the problem is:")
    print(current_position)
else:
    print("No solution found.")
def hiding_places(start):
    board = [[9 for i in range(8)] for i in range(8)]  # Initialize board
    add_coords = [coords(start)]
    i = -1
    while any(9 in row for row in board):
        i += 1
        for coord in add_coords:
            x, y = coord
            if board[x][y] == 9:
                board[x][y] = i
        next_coords = []
        for coord in add_coords:
            next_coords.extend(possible_squares(*coord))
        add_coords = next_coords
    max_indices = []ss
    for j in range(8):
        for k in range(8):
            if board[j][k] == i:
                max_indices.append((j, k))
    chess_indices = [chess_coords(*coord) for coord in max_indices]
    print(i, *(sorted(chess_indices, key=lambda x: x[1], reverse=True)))   
def possible_squares(x, y):
    possible = []
    if 0 <= x-2 <= 7:
        if 0 <= y-1 <= 7:
            possible.append((x-2, y-1))
        if 0 <= y+1 <= 7:
            possible.append((x-2, y+1))
    if 0 <= x+2 <= 7:
        if 0 <= y-1 <= 7:
            possible.append((x+2, y-1))
        if 0 <= y+1 <= 7:
            possible.append((x+2, y+1))
    if 0 <= x-1 <= 7:
        if 0 <= y-2 <= 7:
            possible.append((x-1, y-2))
        if 0 <= y+2 <= 7:
            possible.append((x-1, y+2))
    if 0 <= x+1 <= 7:
        if 0 <= y-2 <= 7:
            possible.append((x+1, y-2))
        if 0 <= y+2 <= 7:
            possible.append((x+1, y+2))
    return possible        
def coords(square):
    rows = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    return ((int(square[1]) - 1, rows[square[0]]))
def chess_coords(x, y):
    rows = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    return rows[y] + str(x + 1)
def print_board(board):
    for i in range(7, -1, -1):
        print(board[i])
    
for i in range(int(input())):
    start = input()
    hiding_places(start)

for _ in range(int(input())):

    cols, rows = map(int, input().split())
    
    grid = [[0 for i in range(cols)] for i in range(rows)]
    
    n, m = map(int, input().split())

    direction = {}
    rpos = {}
    for rn in range(1, n+1):
        j, i, d = input().split()
        direction[rn] = d
        i, j = map(int, [i, j])
        i, j = i-1, j-1 # Switch to zero-indexing
        grid[i][j] = rn
        rpos[rn] = [i, j]

    directions = "NESW"
    d_effect = {
        'N': (1, 0),
        'E': (0, 1),
        'S': (-1, 0),
        'W': (0, -1)
    }
    error = False
    for mn in range(m):
        rn, move, rep = input().split()
        if error:
            continue
        rn, rep = map(int, [rn, rep])
        if move == 'L':
            direction[rn] = directions[(directions.index(direction[rn]) - 1 * rep) % 4]
        elif move == 'R':
            direction[rn] = directions[(directions.index(direction[rn]) + 1 * rep) % 4]
        elif move == 'F':
            for i in range(rep):
                xpos, ypos = rpos[rn]
                movement = d_effect[direction[rn]]
                xpos += movement[0]
                ypos += movement[1]

                # bounds checking
                if xpos < 0 or xpos >= rows or ypos < 0 or ypos >= cols:
                    print(f"Robot {rn} crashes into the wall")
                    error = True
                    break

                # update grid
                spot = grid[xpos][ypos]
                if spot == 0:
                    grid[xpos][ypos] = rn
                    grid[rpos[rn][0]][rpos[rn][1]] = 0
                    rpos[rn] = [xpos, ypos]
                else:
                    print(f"Robot {rn} crashes into robot {spot}")
                    error = True
                    break
    if not error:
        print("OK")
            
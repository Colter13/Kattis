# Function to find the words in a crossword grid
def find_words(grid, rows, columns, words):
    for i in range(rows):
        for j in range(columns - 1):
            if grid[i][j].isalpha() and (j == 0 or grid[i][j-1] == '#') and grid[i][j+1] != '#':
                current_word = grid[i][j:j+2]
                increment = 2
                if increment + j < columns:
                    next_ch = grid[i][j+increment]
                else:
                    next_ch = '#'   # Arbitrary non-alpha
                while next_ch.isalpha():
                    current_word += next_ch
                    increment += 1
                    if increment + j < columns:
                        next_ch = grid[i][j+increment]
                    else:
                        break
                words.append(current_word)
    return words

# Initialize words list
words = []

# Input
rows, columns = map(int, input().split())
grid = [input() for i in range(rows)]

# Find Across
words = find_words(grid, rows, columns, words)

# Transpose the matrix and find Up
rows, columns = columns, rows
grid = [''.join(row) for row in zip(*grid)]
words = find_words(grid, rows, columns, words)

# Output
print(sorted(words)[0])
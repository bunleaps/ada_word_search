def preprocess_grid(grid):
    # Preprocess rows and columns to speed up word searches.
    rows = ["".join(row) for row in grid]
    cols = ["".join([grid[row][col] for row in range(len(grid))]) for col in range(len(grid[0]))]
    return rows, cols


def dp_find_word(grid, word, rows, cols):
    # Search for a word using preprocessed rows and columns."""
    # Check in rows (horizontal search)
    for r_idx, row in enumerate(rows):
        start = row.find(word)
        if start != -1:
            return (r_idx, start), (r_idx, start + len(word) - 1)
        # Check reversed word
        start = row.find(word[::-1])
        if start != -1:
            return (r_idx, start + len(word) - 1), (r_idx, start)

    # Check in columns (vertical search)
    for c_idx, col in enumerate(cols):
        start = col.find(word)
        if start != -1:
            return (start, c_idx), (start + len(word) - 1, c_idx)
        # Check reversed word
        start = col.find(word[::-1])
        if start != -1:
            return (start + len(word) - 1, c_idx), (start, c_idx)

    return None  # Word not found


def dp_solve_wordsearch(grid, words):
    # Solve the wordsearch using Dynamic Programming.
    rows, cols = preprocess_grid(grid)
    found_words = {}
    for word in words:
        location = dp_find_word(grid, word, rows, cols)
        if location:  # Only store found words
            found_words[word] = location
    return found_words


def find_word_horizontal(grid, word):
    # Search for a word horizontally in the grid.
    for row in range(len(grid)):
        for col in range(len(grid[0]) - len(word) + 1):
            # Check forward
            if grid[row][col : col + len(word)] == list(word):
                return (row, col), (row, col + len(word) - 1)
            # Check backward
            if grid[row][col : col + len(word)] == list(word[::-1]):
                return (row, col + len(word) - 1), (row, col)
    return None


def find_word_vertical(grid, word):
    # Search for a word vertically in the grid.
    for col in range(len(grid[0])):
        for row in range(len(grid) - len(word) + 1):
            # Check downward
            if [grid[row + i][col] for i in range(len(word))] == list(word):
                return (row, col), (row + len(word) - 1, col)
            # Check upward
            if [grid[row + i][col] for i in range(len(word))] == list(word[::-1]):
                return (row + len(word) - 1, col), (row, col)

def naive_solve_wordsearch(grid, words):
    # Solve the wordsearch using the naïve method.
    found_words = {}
    for word in words:
        location = find_word_horizontal(grid, word) or find_word_vertical(grid, word)
        if location:  # Only add the word if it is found
            found_words[word] = location
    return found_words


def print_grid(grid):
    # Print the crossword grid with numbers and a border.
    # rows = len(grid)
    cols = len(grid[0])

    # Print column numbers
    print("   " + " ".join(f"{col:2}" for col in range(cols)))
    print("  +" + "---" * cols + "+")

    # Print each row with its row number
    for r_idx, row in enumerate(grid):
        print(f"{r_idx:2}|" + " ".join(f" {cell}" for cell in row) + " |")
    
    print("  +" + "---" * cols + "+")  # Print bottom border


if __name__ == "__main__":
    category = 'animals'  # Example category
    grid_file = f'word_search/{category}/{category}_2.txt'

    # Read the grid from the file
    with open(grid_file, 'r') as f:
        wordsearch_grid = [line.strip().split() for line in f.readlines()]

    # Read words from file
    with open(f"words/{category}.txt", "r") as file:
        word_list = [line.strip() for line in file]

    print("Wordsearch grid:")
    print_grid(wordsearch_grid)

    print("\nSolving with Dynamic Programming:")
    dp_found = dp_solve_wordsearch(wordsearch_grid, word_list)
    for word, location in dp_found.items():
        print(f"{word}: {location}")

    print("\nSolving with Naïve Method:")
    naive_found = naive_solve_wordsearch(wordsearch_grid, word_list)
    for word, location in naive_found.items():
        print(f"{word}: {location}")

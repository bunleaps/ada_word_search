def preprocess_grid(grid):
    # Preprocess rows and columns to speed up word searches.
    rows = ["".join(row) for row in grid]
    cols = ["".join([grid[row][col] for row in range(len(grid))]) for col in range(len(grid[0]))]
    return rows, cols


def dp_find_word(grid, word, rows, cols):
    # Search for a word using preprocessed rows and columns.
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
        found_words[word] = location if location else "Not found"
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
    # Print the crossword grid.
    for row in grid:
        print(" ".join(row))


# Example 15x15 Grid and Words
if __name__ == "__main__":
    wordsearch_grid = [
        ["a", "p", "p", "l", "e", "s", "e", "n", "t", "a", "n", "a", "h", "o", "t"],
        ["c", "a", "t", "r", "e", "e", "s", "m", "i", "l", "e", "r", "i", "c", "e"],
        ["p", "e", "a", "c", "h", "e", "s", "m", "e", "t", "r", "a", "i", "n", "y"],
        ["e", "o", "l", "i", "v", "e", "s", "e", "a", "r", "t", "h", "l", "e", "m"],
        ["b", "a", "n", "a", "n", "a", "s", "i", "s", "l", "a", "n", "d", "t", "i"],
        ["a", "v", "o", "c", "a", "d", "o", "c", "l", "o", "u", "d", "s", "o", "n"],
        ["r", "a", "i", "n", "b", "o", "w", "t", "r", "a", "i", "n", "c", "o", "w"],
        ["a", "l", "m", "o", "n", "d", "s", "p", "e", "a", "r", "t", "h", "e", "y"],
        ["p", "i", "n", "e", "a", "p", "p", "l", "e", "e", "g", "o", "a", "t", "s"],
        ["g", "r", "a", "p", "e", "s", "c", "r", "i", "b", "e", "l", "o", "n", "e"],
        ["o", "r", "a", "n", "g", "e", "b", "e", "a", "c", "h", "e", "s", "i", "n"],
        ["p", "e", "a", "r", "s", "o", "r", "c", "h", "a", "r", "d", "h", "o", "p"],
        ["w", "a", "t", "e", "r", "m", "e", "l", "o", "n", "a", "l", "e", "e", "p"],
        ["s", "a", "p", "p", "l", "e", "p", "e", "a", "r", "t", "r", "u", "n", "k"],
        ["m", "a", "n", "g", "o", "t", "e", "r", "r", "a", "i", "n", "f", "a", "l"],
    ]

    word_list = [
        "apple",
        "peach",
        "banana",
        "grape",
        "orange",
        "pear",
        "watermelon",
        "rain",
        "cloud",
        "tree",
        "train",
        "videos",
        "happy"
    ]

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

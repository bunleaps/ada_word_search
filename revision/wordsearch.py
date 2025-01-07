def find_word_horizontal(grid, word):
    """Search for a word horizontally in the grid."""
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
    """Search for a word vertically in the grid."""
    for col in range(len(grid[0])):
        for row in range(len(grid) - len(word) + 1):
            # Check downward
            if [grid[row + i][col] for i in range(len(word))] == list(word):
                return (row, col), (row + len(word) - 1, col)
            # Check upward
            if [grid[row + i][col] for i in range(len(word))] == list(word[::-1]):
                return (row + len(word) - 1, col), (row, col)
    return None


def solve_crossword(grid, words):
    """Solve the crossword by finding each word in the grid."""
    found_words = {}
    for word in words:
        location = find_word_horizontal(grid, word)
        if not location:
            location = find_word_vertical(grid, word)
        if location:
            found_words[word] = location
        else:
            found_words[word] = None  # Word not found
    return found_words


def print_grid(grid):
    """Print the crossword grid."""
    for row in grid:
        print(" ".join(row))


# Example 15x15 Grid and Words
if __name__ == "__main__":
    crossword_grid = [
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
    ]

    print("Crossword grid:")
    print_grid(crossword_grid)

    found = solve_crossword(crossword_grid, word_list)
    print("\nWord locations:")
    for word, location in found.items():
        if location:
            print(f"{word}: {location}")
        else:
            print(f"{word}: Not found")

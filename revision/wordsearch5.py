import os
import time
import tracemalloc

def read_words(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def read_word_search(file_path):
    with open(file_path, 'r') as f:
        return [line.strip().split() for line in f]

def preprocess_grid(grid):
    rows = ["".join(row) for row in grid]
    cols = ["".join([grid[row][col] for row in range(len(grid))]) for col in range(len(grid[0]))]
    return rows, cols

def dp_find_word(grid, word, rows, cols):
    for r_idx, row in enumerate(rows):
        start = row.find(word)
        if start != -1:
            return (r_idx, start), (r_idx, start + len(word) - 1)
        start = row.find(word[::-1])
        if start != -1:
            return (r_idx, start + len(word) - 1), (r_idx, start)

    for c_idx, col in enumerate(cols):
        start = col.find(word)
        if start != -1:
            return (start, c_idx), (start + len(word) - 1, c_idx)
        start = col.find(word[::-1])
        if start != -1:
            return (start + len(word) - 1, c_idx), (start, c_idx)

    return None

def dp_solve_wordsearch(grid, words):
    rows, cols = preprocess_grid(grid)
    found_words = {}
    for word in words:
        location = dp_find_word(grid, word, rows, cols)
        if location:
            found_words[word] = location
    return found_words

def find_word_horizontal(grid, word):
    for row in range(len(grid)):
        for col in range(len(grid[0]) - len(word) + 1):
            if grid[row][col:col + len(word)] == list(word):
                return (row, col), (row, col + len(word) - 1)
            if grid[row][col:col + len(word)] == list(word[::-1]):
                return (row, col + len(word) - 1), (row, col)
    return None

def find_word_vertical(grid, word):
    for col in range(len(grid[0])):
        for row in range(len(grid) - len(word) + 1):
            if [grid[row + i][col] for i in range(len(word))] == list(word):
                return (row, col), (row + len(word) - 1, col)
            if [grid[row + i][col] for i in range(len(word))] == list(word[::-1]):
                return (row + len(word) - 1, col), (row, col)
    return None

def naive_solve_wordsearch(grid, words):
    found_words = {}
    for word in words:
        location = find_word_horizontal(grid, word) or find_word_vertical(grid, word)
        if location:
            found_words[word] = location
    return found_words

def print_grid(grid):
    cols = len(grid[0])
    grid_str = ""

    grid_str += "   " + " ".join(f"{col:2}" for col in range(cols)) + "\n"
    grid_str += "  +" + "---" * cols + "+\n"

    for r_idx, row in enumerate(grid):
        grid_str += f"{r_idx:2}|" + " ".join(f" {cell}" for cell in row) + " |\n"
    
    grid_str += "  +" + "---" * cols + "+\n"
    return grid_str

def solve_word_searches(input_dir, output_dir):
    for category in os.listdir(input_dir):
        category_path = os.path.join(input_dir, category)
        if os.path.isdir(category_path):
            for file_name in os.listdir(category_path):
                if file_name.endswith('.txt'):
                    grid_file = os.path.join(category_path, file_name)
                    word_list = read_words(os.path.join('words', f"{category}.txt"))
                    wordsearch_grid = read_word_search(grid_file)

                    print(f"Solving {grid_file}...")

                    # Measure DP solution
                    tracemalloc.start()
                    dp_start_time = time.time()
                    dp_found = dp_solve_wordsearch(wordsearch_grid, word_list)
                    dp_end_time = time.time()
                    dp_current, dp_peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()

                    dp_duration = dp_end_time - dp_start_time
                    dp_memory_used = dp_peak / 10**6  # Convert to MB

                    # Measure Naive solution
                    tracemalloc.start()
                    naive_start_time = time.time()
                    naive_found = naive_solve_wordsearch(wordsearch_grid, word_list)
                    naive_end_time = time.time()
                    naive_current, naive_peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()

                    naive_duration = naive_end_time - naive_start_time
                    naive_memory_used = naive_peak / 10**6  # Convert to MB

                    # Save results
                    solved_file = grid_file.replace('.txt', '_solved.txt')
                    with open(solved_file, 'w') as f:
                        f.write("Wordsearch grid:\n")
                        f.write(print_grid(wordsearch_grid))
                        
                        f.write("Dynamic Programming Solution:\n")
                        for word, location in dp_found.items():
                            f.write(f"{word}: {location}\n")
                        f.write(f"\nDP Time taken: {dp_duration:.4f} seconds\n")
                        f.write(f"DP Memory used: {dp_memory_used:.2f} MB\n")

                        f.write("\nNaïve Method Solution:\n")
                        for word, location in naive_found.items():
                            f.write(f"{word}: {location}\n")
                        f.write(f"\nNaïve Time taken: {naive_duration:.4f} seconds\n")
                        f.write(f"Naïve Memory used: {naive_memory_used:.2f} MB\n")

                    print(f"Solved {grid_file} and saved to {solved_file}")

if __name__ == "__main__":
    input_dir = 'word_search_10_100'
    output_dir = 'solved_word_search'
    solve_word_searches(input_dir, output_dir)

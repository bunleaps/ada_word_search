import os
import random
import string

def read_words(file_path):
    try:
        with open(file_path, 'r') as f:
            words = [line.strip() for line in f]
            print(f"Read {len(words)} words from {file_path}")
            return words
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return []

def create_word_search(words, size=10):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    max_attempts = 1000  # Limit the number of attempts to place each word
    
    for word in words:
        placed = False
        attempts = 0
        while not placed and attempts < max_attempts:
            direction = random.choice(directions)
            start_row = random.randint(0, size - 1)
            start_col = random.randint(0, size - 1)
            end_row = start_row + direction[0] * len(word)
            end_col = start_col + direction[1] * len(word)
            if 0 <= end_row < size and 0 <= end_col < size:
                if all(grid[start_row + i * direction[0]][start_col + i * direction[1]] in (' ', letter) 
                       for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[start_row + i * direction[0]][start_col + i * direction[1]] = letter
                    placed = True
            attempts += 1
        
        if not placed:
            print(f"Failed to place the word '{word}' after {max_attempts} attempts.")
    
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(string.ascii_lowercase)
    
    return grid

def save_word_search(grid, category, num, output_dir):
    try:
        os.makedirs(os.path.join(output_dir, category), exist_ok=True)
        file_path = os.path.join(output_dir, category, f"{category}_{num}.txt")
        with open(file_path, 'w') as f:
            for row in grid:
                f.write(' '.join(row) + '\n')
        print(f"Saved word search to {file_path}")
    except Exception as e:
        print(f"Failed to save {file_path}: {e}")

def generate_word_searches(input_dir, output_dir, grid_size=10, num_files=3):
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith('.txt'):
                category = file_name.replace('.txt', '')
                words = read_words(os.path.join(input_dir, file_name))
                for i in range(1, num_files + 1):
                    grid = create_word_search(words, size=grid_size)
                    save_word_search(grid, category, i, output_dir)
                    print(f"Generated {category}_{i}.txt")
    except Exception as e:
        print(f"Error generating word searches: {e}")

# Parameters
input_dir = 'words'
output_dir = 'word_search_80_100'
grid_size = 80  # Set the grid size here
num_files = 100   # Set the number of files to generate here

generate_word_searches(input_dir, output_dir, grid_size, num_files)

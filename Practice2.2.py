def count_squares(x):
    total_squares = 0
    for i in range(1, x + 1):
        total_squares += i ** 2
    return total_squares

x = 4  # Replace this with the size of the grid (e.g., 2 for a 2x2 grid)
num_squares = count_squares(x)
print(f"A {x}x{x} grid has {num_squares} squares.")

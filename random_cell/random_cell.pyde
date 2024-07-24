# import random

# def setup():
#     size(800, 800)  # Set the size of the window
#     global grid, width, height, start_point, current_row, scale_grid
#     width = 400  # Set the width of the grid
#     height = 400  # Set the height of the grid
#     start_point = (0, 0)  # Set the starting point
#     current_row = 0
#     scale_grid = 2
#     grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize the grid with all 0s
#     grid[start_point[1]][start_point[0]] = 1  # Set the start point in the grid
#     grid[0][5] = 1  # Set the start point in the grid
    
#     # frameRate(30)  # Adjust the speed of the sketch for visualization
#     draw_grid()



# def calc_grid():
#     global current_row

#     if current_row < height - 1:
#         next_row = [0] * width
#         for i in range(width):
#             if i == 0:
#                 next_row[i] = grid[current_row][i+1]
#             elif i == width - 1:
#                 next_row[i] = grid[current_row][i-1]
#             else:
#                 window = grid[current_row][i-1:i+2]
#                 if window == [1, 1, 1]:
#                     next_row[i] = 0
#                 elif window == [1, 1, 0]:
#                     next_row[i] = 1
#                 elif window == [1, 0, 1]:
#                     next_row[i] = 0
#                 elif window == [1, 0, 0]:
#                     next_row[i] = 1
#                 elif window == [0, 1, 1]:
#                     next_row[i] = 0
#                 elif window == [0, 1, 0]:
#                     next_row[i] = 1
#                 elif window == [0, 0, 1]:
#                     next_row[i] = 1
#                 elif window == [0, 0, 0]:
#                     next_row[i] = 0
#         grid[current_row + 1] = next_row
#         current_row += 1
#         draw_grid()

# def flip_value(input_value, probability):
#     if not (input_value in [0, 1]):
#         raise ValueError("input_value must be 0 or 1")
#     if not (0 <= probability <= 1):
#         raise ValueError("probability must be between 0 and 1")

#     if random.random() < probability:
#         return 1 - input_value
#     else:
#         return input_value
# def draw_grid():
#     background(255)
#     stroke(0)
#     fill(0)
#     for y in range(height):
#         for x in range(width):
#             if grid[y][x] == 1:
#                 rect(x * scale_grid, y * scale_grid, scale_grid, scale_grid)
# def draw():
#     calc_grid()

import random
def reset():
    width = 400  # Set the width of the grid
    height = 400  # Set the height of the grid
    start_point = (0, 0)  # Set the starting point
    current_row = 0
    scale_grid = 2
    probability = 0.0001
    grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize the grid with all 0s
    grid[start_point[1]][start_point[0]] = 1  # Set the start point in the grid
    grid[0][5] = 1  # Set the start point in the grid
    
    # frameRate(30)  # Adjust the speed of the sketch for visualization
    draw_grid()
def setup():
    size(800, 800)  # Set the size of the window
    global grid, width, height, start_point, current_row, scale_grid, probability
    width = 400  # Set the width of the grid
    height = 400  # Set the height of the grid
    start_point = (0, 0)  # Set the starting point
    current_row = 0
    scale_grid = 2
    probability = 0.0001
    grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize the grid with all 0s
    grid[start_point[1]][start_point[0]] = 1  # Set the start point in the grid
    grid[0][5] = 1  # Set the start point in the grid
    # reset()
    # frameRate(30)  # Adjust the speed of the sketch for visualization
    draw_grid()



def calc_grid():
    global current_row

    if current_row < height - 1:
        next_row = [0] * width
        for i in range(width):
            if i == 0:
                next_row[i] = grid[current_row][i+1]
            elif i == width - 1:
                next_row[i] = grid[current_row][i-1]
            else:
                window = grid[current_row][i-1:i+2]
                if window == [1, 1, 1]:
                    next_row[i] = 0
                elif window == [1, 1, 0]:
                    next_row[i] = 1
                elif window == [1, 0, 1]:
                    next_row[i] = 0
                elif window == [1, 0, 0]:
                    next_row[i] = 1
                elif window == [0, 1, 1]:
                    next_row[i] = 0
                elif window == [0, 1, 0]:
                    next_row[i] = 1
                elif window == [0, 0, 1]:
                    next_row[i] = 1
                elif window == [0, 0, 0]:
                    next_row[i] = 0
        grid[current_row + 1] = next_row
        current_row += 1
        draw_grid()

def flip_value(input_value, probability):
    if not (input_value in [0, 1]):
        raise ValueError("input_value must be 0 or 1")
    if not (0 <= probability <= 1):
        raise ValueError("probability must be between 0 and 1")

    if random.random() < probability:
        return 1 - input_value
    else:
        return input_value
def draw_grid():
    background(255)
    stroke(0)
    fill(0)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                rect(x * scale_grid, y * scale_grid, scale_grid, scale_grid)
def draw():
    calc_grid()

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


def setup():
    size(800, 800)  # Set the size of the window
    global  running,rule_number,  width, height,scale_grid, changer
    changer = 0
    running = False
    rule_number = 22
    width = 400  # Set the width of the grid
    height = 400  # Set the height of the grid
    scale_grid = 2

    reset()

def mousePressed():
    global running, rule_number
    running = not running
    print("mousePressed")
    rule_number +=1
    reset() 

def reset():
    
    global grid,start_point, current_row, probability, rule
    rule = convert_to_rule([30,54,60,62,90,94,102,110,122,126,150,158,182,188,190,220,222,250][rule_number%18])
    
    start_point = (width//2, 0)  # Set the starting point
    current_row = 0
    probability = 0.0001
    grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize the grid with all 0s
    grid[start_point[1]][start_point[0]] = 1  




def convert_to_rule(decimal):
    # array_binary =  list("{:0>8}".format(str(bin(decimal  % 255))[2:]))
    # return  
    p = [int(x) for x in list("{:08b}".format(decimal % 255)) ]
    print(p)
    return p
def calc_grid():
    global current_row
    global rule
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
                    next_row[i] = rule[0]
                elif window == [1, 1, 0]:
                    next_row[i] = rule[1]
                elif window == [1, 0, 1]:
                    next_row[i] = rule[2]
                elif window == [1, 0, 0]:
                    next_row[i] = rule[3]
                elif window == [0, 1, 1]:
                    next_row[i] = rule[4]
                elif window == [0, 1, 0]:
                    next_row[i] = rule[5]
                elif window == [0, 0, 1]:
                    next_row[i] = rule[6]
                elif window == [0, 0, 0]:
                    next_row[i] = rule[7]
        grid[current_row + 1] = next_row
        current_row += 1
        draw_grid()
        # if running:
        #     reset() 
            # running = False
        
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
    background(0)
    # stroke(0)
    noStroke()
    # fill(0)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                rect(x * scale_grid, y * scale_grid, scale_grid, scale_grid)
def draw():
    global changer,rule
    if changer % 10 ==0:
        rule = convert_to_rule(random.choice([30,54,60,62,90,94,102,110,122,126,150,158,182,188,190,220,222,250]))

    calc_grid()
    changer += 1
    

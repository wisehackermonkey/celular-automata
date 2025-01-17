import random


def setup():
    size(800, 800)  # Set the size of the window
    global  running,rule_number,  width, height,scale_grid, changer, xoff,yoff,zoff, CHANGE_INTERVAL
    CHANGE_INTERVAL = 2000#random.randint(1,20)
    changer = 0
    running = False
    rule_number = 22
    width = 400  # Set the width of the grid
    height = 400  # Set the height of the grid
    scale_grid = 2

    xoff = 0.0 # used for perlin noise
    yoff = 0.0
    zoff = 0.0 
    background(0)
    # stroke(0)
    noStroke()
    # fill(0)
    reset()

def mousePressed():
    global running, rule_number, rule
    running = not running
    print("mousePressed",rule)
    rule_number +=1
    rule = convert_to_rule([30,54,60,62,90,94,102,110,122,126,150,158,182,188,190,220,222,250][rule_number%18])

    # reset() 
def perlin():
    global xoff
    xoff += 0.01
    n = noise(xoff) * width
    return n
def reset():
    
    global grid,start_point, current_row, rule
    rule = convert_to_rule([30,54,60,62,90,94,102,110,122,126,150,158,182,188,190,220,222,250][rule_number%18])
    
    start_point = (width//2, 0)  # Set the starting point
    current_row = 0
    grid = [[0 for _ in range(width)] for _ in range(height)]  # Initialize the grid with all 0s
    grid[start_point[1]][start_point[0]] = 1  


    background(0)


def convert_to_rule(decimal): 
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
                    fill(0)
                elif window == [1, 1, 0]:
                    next_row[i] = rule[1]
                    fill(32)
                elif window == [1, 0, 1]:
                    next_row[i] = rule[2]
                    fill(64)
                elif window == [1, 0, 0]:
                    next_row[i] = rule[3]
                    fill(96)
                elif window == [0, 1, 1]:
                    next_row[i] = rule[4]
                    fill(160)
                elif window == [0, 1, 0]:
                    next_row[i] = rule[5]
                    fill(192)
                elif window == [0, 0, 1]:
                    next_row[i] = rule[6]
                    fill(224)
                elif window == [0, 0, 0]:
                    next_row[i] = rule[7]
                    fill(255)
        grid[current_row + 1] = next_row
        current_row += 1
        draw_grid()
  
def draw_grid():
    
    # for y in range(height):
    global xoff, yoff, zoff
    xoff += 0.05
    r = noise(xoff) * 255
    xoff += 0.1

    g  = noise(yoff) * 255
    yoff += 1.01

    b  = noise(zoff) * 255
    zoff *= 1.01

    for x in range(width):
        y = current_row
        if grid[current_row][x] == 1:
            # fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            # fill(r,g,b)
            rect(x * scale_grid, y * scale_grid, scale_grid, scale_grid)
def draw():
    global changer,rule, CHANGE_INTERVAL
    if changer % CHANGE_INTERVAL ==0:
        rule = convert_to_rule(random.choice([30,54,60,62,90,94,102,110,122,126,150,158,182,188,190,220,222,250]))

    calc_grid()
    changer += 1
    

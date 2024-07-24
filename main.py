# prompt
#----------

create a   processing.org python sketch
intalize a grid (2d array of size hieght and width), init as all 0's default is 
set start point to start_point x,y 
set current row = 0
set scale_grid to 4
make a  function that iterates over each row of the grid
and impliments following logic
create a temporary array called next_row default to [0,]
for a window size of  3
example:
 0,1,2,3,4,5 - index
[1,0,1,0,0,0,...] - grid
index = 0
window = [1,0,1] or indexes 0,1,2

edge cases
for each index in grid[0]
if index = 0
  set index + 1 and skip rest of loop
if index +1 = width:
    exit out of loop
if all items are [1,1,1]-> temparr[index+1] =[0]
if left [1,1,0] -> temparr[index+1] = [1]
if not_middle [1,0,1] -> temparr[index+1] = [0]
if south_west [1,0,0] -> temparr[index+1] = [1]
if mid_left [0,1,1] -> temparr[index+1] = [0]
if middle [0,1,0] -> temparr[index+1] = [1]
if south_east [0,0,1] -> temparr[index+1] = [1]
if non [0,0,0] -> temparr[index+1] = [0]


set current row +1

loop untill height is reached

 create a function that takes a input of 1 or 0 , and a probability between 0 and 1
 return flip !value if probability is over .5
 
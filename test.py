import math
import pygame
import numpy



pieces = [
[1,2,0, #les jaunes
 2,1,2,
 0,0,0],

[1,1,0,
 0,1,2,
 0,0,0],

[1,2,0,
 0,1,1,
 0,0,0],

[0,0,1,
 1,2,1,
 0,0,0],
 
[0,0,1,
 1,1,2,
 0,0,0],

[0,0,2,
 1,1,1,
 0,0,0],

[0,0,1,
 2,1,1,
 0,0,0],

[0,2,0,
 1,1,1,
 0,0,0],
 
[0,1,0,
 1,1,2,
 0,0,0]
]

grid_X = 6
grid_Y = 6

grid = [
    0,0,0,0,1,0,
    1,0,1,0,0,1,
    0,0,0,1,0,0,
    0,1,0,0,0,1,
    0,0,1,0,0,0,
    1,0,0,0,0,1
]


rot_list = [

    [0,1,2,
     3,4,5,
     6,7,8],

    [3,0,6,
     4,1,7,
     5,2,8],

    [5,4,3,
     2,1,0,
     6,7,8],

    [2,5,8,
     1,4,7,
     0,3,6],

    [2,1,0,
     5,4,3,
     8,7,6],
        
    [0,3,6,
     1,4,7,
     2,5,8],

    [3,4,5,
    0,1,2,
    6,7,8],

    [5,2,8,
     4,1,7,
     3,0,6]
    ]

def load_piece(piece_to_load, rotation):
    
    piece_load = []
    for i in range(9):
        piece_load.append(piece_to_load[rotation[i]])

    return piece_load

def piece_grid(piece_load,y,x):
    grid_piece = []
    for i in range(grid_X*grid_Y):
      grid_piece.append(0)
    for Y in range(3):
        for X in range(3):
            if(x+X < grid_X and y+Y < grid_Y):
                grid_piece[x+X+(y+Y)*grid_X] = piece_load[X+Y*3]
    return grid_piece
    
 


if (grid_X*grid_Y == len(grid)):
    well_place = []
    for piece in range(len(pieces)):
        piece_well_place = []
        for sym in range(2):
            for rot in range(4):
                piece_load = load_piece(pieces[piece], rot_list[rot+sym*4])
                print(piece_load)
                for y in range(grid_Y-1):
                    for x in range(grid_X-1):
                        good_pos = 0
                        for pos in range(9):
                            if(x+(pos%3) < grid_X and y + numpy.floor(pos/3) < grid_Y and piece_load[pos] - 1 == grid[int(x+(pos%3) + (y + numpy.floor(pos/3.1))*grid_X)]):
                                good_pos += 1
                        print(good_pos)
                        if (good_pos == 4):
                            well_place.append(piece_grid(piece_load,y,x))

        piece_well_place.append(well_place)
        print(piece_well_place)


else: 
    print("error : size of grid")
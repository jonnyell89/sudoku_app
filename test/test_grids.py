empty_grid = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,]

]

valid_grid = [

    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [4, 5, 6, 7, 8, 9, 1, 2, 3], 
    [7, 8, 9, 1, 2, 3, 4, 5, 6], 
    [2, 3, 1, 5, 6, 4, 8, 9, 7], 
    [5, 6, 4, 8, 9, 7, 2, 3, 1], 
    [8, 9, 7, 2, 3, 1, 5, 6, 4], 
    [3, 1, 2, 6, 4, 5, 9, 7, 8], 
    [6, 4, 5, 9, 7, 8, 3, 1, 2], 
    [9, 7, 8, 3, 1, 2, 6, 4, 5]

]

invalid_row = [

    [0, 0, 0, 0, 7, 0, 6, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 1, 5, 0, 8, 0, 0, 0, 9],
    [4, 3, 0, 0, 0, 0, 5, 8, 0],
    [5, 6, 0, 0, 0, 1, 0, 3, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [2, 0, 0, 7, 2, 5, 1, 0, 4],
    [0, 0, 0, 0, 0, 0, 2, 9, 0]

]

invalid_col = [

    [0, 6, 5, 0, 0, 0, 0, 8, 0],
    [0, 0, 3, 1, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 7, 2, 0, 0, 0],
    [0, 0, 1, 4, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 6, 0, 9],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 9, 4, 0],
    [2, 0, 0, 0, 0, 0, 7, 0, 3],
    [4, 0, 0, 5, 0, 0, 0, 0, 1]

]

invalid_subgrid = [

    [8, 0, 1, 0, 5, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 8, 0, 0, 0],
    [6, 0, 4, 0, 0, 0, 2, 0, 7],
    [0, 9, 0, 0, 0, 0, 1, 0, 2],
    [5, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 4, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 9, 3, 0, 0],
    [7, 0, 0, 1, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 7, 4, 0, 0, 0]

]

easy_grid = [

    [5, 6, 0, 0, 1, 0, 0, 0, 7],
    [3, 4, 0, 6, 8, 0, 9, 1, 0],
    [0, 9, 7, 0, 5, 4, 6, 8, 3],
    [2, 0, 9, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 6, 0, 0, 9, 8],
    [0, 8, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0, 1, 0, 0, 0],
    [9, 0, 6, 3, 0, 5, 0, 7, 1],
    [8, 5, 0, 0, 2, 6, 0, 0, 0]
    
]

medium_grid = [

    [0, 7, 0, 0, 0, 5, 1, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 1, 3, 7, 2, 6, 8, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 8, 4, 0, 9, 0, 0],
    [9, 0, 0, 1, 0, 0, 7, 0, 8],
    [0, 0, 8, 0, 3, 0, 0, 4, 0],
    [0, 0, 0, 0, 8, 9, 6, 5, 1]

]

hard_grid = [

    [9, 2, 6, 8, 0, 1, 0, 0, 5],
    [8, 0, 0, 0, 4, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 1, 0, 7, 0, 4, 0, 3, 8],
    [0, 0, 0, 5, 9, 0, 0, 6, 2],
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 1, 0],
    [0, 0, 2, 9, 0, 5, 6, 0, 0],
    [0, 0, 7, 0, 8, 0, 2, 0, 4]

]

expert_grid = [

    [0, 0, 1, 0, 0, 0, 3, 6, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [3, 0, 0, 0, 5, 6, 0, 8, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [1, 0, 0, 0, 3, 8, 0, 5, 0],
    [0, 0, 0, 1, 0, 0, 0, 9, 0],
    [0, 0, 7, 0, 6, 9, 0, 0, 5],
    [6, 0, 0, 2, 0, 0, 0, 0, 0]

]

master_grid = [

    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [7, 0, 3, 0, 8, 5, 4, 0, 0],
    [9, 2, 0, 3, 7, 0, 0, 0, 0],
    [0, 5, 0, 0, 9, 0, 0, 3, 0],
    [0, 0, 4, 0, 0, 3, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 7, 4, 5],
    [6, 0, 2, 5, 0, 0, 0, 8, 4],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 8, 2, 0, 0, 1, 0]

]

extreme_grid = [

    [0, 6, 1, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 4, 0, 0, 8],
    [0, 0, 0, 0, 1, 0, 5, 0, 0],
    [7, 5, 0, 8, 0, 0, 0, 0, 0],
    [0, 9, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 4, 2, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 3, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 8, 0, 0, 4, 0]

]

brute_force = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]

]

mit = [

    [0, 0, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 3, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 3, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 5],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 0]

]

full_grid = [

    [5, 6, 8, 9, 1, 3, 4, 2, 7],
    [3, 4, 2, 6, 8, 7, 9, 1, 5],
    [1, 9, 7, 2, 5, 4, 6, 8, 3],
    [2, 1, 9, 5, 3, 8, 7, 6, 4],
    [7, 3, 4, 1, 6, 2, 5, 9, 8],
    [6, 8, 5, 4, 7, 9, 1, 3, 2],
    [4, 7, 3, 8, 9, 1, 2, 5, 6],
    [9, 2, 6, 3, 4, 5, 8, 7, 1],
    [8, 5, 1, 7, 2, 6, 3, 4, 9]
    
]

test_grid = [

    [5, 6, 8, 9, 1, 3, 4, 2, 7],
    [3, 4, 2, 6, 8, 7, 9, 1, 5],
    [1, 9, 7, 2, 5, 4, 6, 8, 3],
    [2, 1, 9, 5, 3, 8, 7, 6, 4],
    [7, 3, 4, 1, 6, 2, 5, 9, 8],
    [6, 8, 5, 4, 7, 9, 1, 3, 2],
    [4, 7, 3, 8, 9, 1, 2, 5, 6],
    [9, 2, 6, 3, 4, 5, 8, 7, 1],
    [8, 5, 1, 7, 2, 6, 3, 4, 9]
    
]

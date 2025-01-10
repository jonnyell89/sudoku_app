import pytest
from app.grid import SudokuGrid
from app.library.grids import (
    
    empty_grid, 
    valid_grid, 
    invalid_row, 
    invalid_col, 
    invalid_subgrid, 
    easy_grid, 
    medium_grid, 
    hard_grid, 
    expert_grid, 
    master_grid, 
    extreme_grid, 
    brute_force, 
    mit, 
    full_grid, 

)

def test_empty_grid_initialisation():

    sudoku = SudokuGrid()

    assert len(sudoku.grid) == 9
    assert all(len(row) == 9 for row in sudoku.grid)
    assert all(cell == 0 for row in sudoku.grid for cell in row)

def test_full_grid_initialisation():

    sudoku = SudokuGrid(full_grid)

    grid_diagonal = [5, 4, 7, 5, 6, 9, 2, 7, 9]

    assert all(sudoku.grid[index][index] == grid_diagonal[index] for index in range(9))

def test_get_row():

    sudoku = SudokuGrid(full_grid)

    first_row = [5, 6, 8, 9, 1, 3, 4, 2, 7]

    assert sudoku.get_row(0) == first_row

def test_get_row_out_of_range():

    sudoku = SudokuGrid(full_grid)

    with pytest.raises(ValueError, match="row_index 9 must be within range 0 to 8."):

        sudoku.get_row(9)



def test_get_col():

    sudoku = SudokuGrid(full_grid)

    first_col = [5, 3, 1, 2, 7, 6, 4, 9, 8]

    assert sudoku.get_col(0) == first_col

def test_get_col_out_of_range():

    sudoku = SudokuGrid(full_grid)

    with pytest.raises(ValueError, match="col_index 9 must be within range 0 to 8."):

        sudoku.get_col(9)



def test_get_subgrid():

    sudoku = SudokuGrid(full_grid)

    first_subgrid = [5, 6, 8, 3, 4, 2, 1, 9, 7]

    assert sudoku.get_subgrid(0, 0) == first_subgrid

def test_get_subgrid_edge_case():

    sudoku = SudokuGrid(full_grid)

    last_subgrid = [2, 5, 6, 8, 7, 1, 3, 4, 9]

    assert sudoku.get_subgrid(8, 8) == last_subgrid

def test_get_subgrid_out_of_range():

    sudoku = SudokuGrid(full_grid)

    with pytest.raises(ValueError, match="row_index 9 and col_index 9 must be within range 0 to 8."):

        sudoku.get_subgrid(9, 9)

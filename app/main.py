from typing import List

from app.grid import SudokuGrid
from app.validator import SudokuValidator
from app.generator import SudokuGenerator
from app.recursion import SudokuRecursion
from app.iteration import SudokuIteration

from test.test_grids import (
    
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
    test_grid

)

class SudokuFacade:

    """
    A facade class to manage and coordinate all Sudoku operations.

    It integrates multiple components into a single unified interface.
    
    """

    def __init__(self, test_grid: List[List[int]] = None):

        """
        Initialises SudokuFacade with an optional test grid.

        Parameters:

            test_grid (List[List[int]], optional): A predefined grid for testing purposes.

                Defaults to None, which initialises an empty grid.

        Attributes:

            grid (SudokuGrid): Manages access to the grid.
            validator (SudokuValidator): Validates cell placements and the overall integrity of the grid.
            recursion (SuokduRecursion): Creates or solves the grid using a recursive backtracking algorithm.
            generator (SudokuGenerator): Generates a puzzle by removing cells from the grid according to difficulty level.
            iterative (SudokuIterative): Solves the grid using iterative logical deduction techniques.
        
        """

        self.grid = SudokuGrid(grid=test_grid)
        self.validator = SudokuValidator(self.grid)
        self.recursion = SudokuRecursion(self.grid, self.validator)
        self.generator = SudokuGenerator(self.grid, self.validator, self.recursion)
        self.iteration = SudokuIteration(self.grid, self.validator)



if __name__ == "__main__":

    print("--------------------")

    sudoku = SudokuFacade(test_grid=easy_grid)

    sudoku.grid.print_formatted_grid()

    print("--------------------")

    sudoku.recursion.populate_grid()

    sudoku.grid.print_formatted_grid()

    print("--------------------")

    print(sudoku.validator.is_grid_valid(debug=True))

    print("--------------------")

    sudoku.generator.remove_cells(difficulty_level="easy")

    sudoku.grid.print_formatted_grid()

    print("--------------------")

    print(sudoku.validator.count_empty_cells())

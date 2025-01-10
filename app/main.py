from typing import List

from app.grid import SudokuGrid
from app.validator import SudokuValidator
from app.generator import SudokuGenerator
from app.recursion import SudokuRecursion
from app.iteration import SudokuIteration
from app.utils import print_formatted_grid

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
    computerphile_valid_grid,
    computerphile_invalid_grid,
    demo_grid

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
            iterative (SudokuIterative): Solves a puzzle using iterative logical deduction techniques.
        
        """

        self.grid = SudokuGrid(grid=test_grid)
        self.validator = SudokuValidator(self.grid)
        self.recursion = SudokuRecursion(self.grid, self.validator)
        self.generator = SudokuGenerator(self.grid, self.validator, self.recursion)
        self.iteration = SudokuIteration(self.grid, self.validator)



if __name__ == "__main__":

    print("--------------------")

    sudoku = SudokuFacade()

    sudoku.recursion.populate_grid()

    sudoku.generator.generate_puzzle(target_removal=(81-17))

    print(f"Is uinque solution: {sudoku.recursion.is_solution_unique()}")

    print_formatted_grid(sudoku.grid.grid)

    print(f"Total solutions: {sudoku.recursion.get_total_solutions(max_solutions=100)}")

    print_formatted_grid(sudoku.grid.grid)

    print(f"Number of empty cells: {sudoku.grid.count_empty_cells()}")

    sudoku.iteration.placement_techniques()

    print_formatted_grid(sudoku.grid.grid)

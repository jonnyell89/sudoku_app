import random

from app.grid import SudokuGrid
from app.validator import SudokuValidator

class SudokuRecursion:

    """
    A class to fill or solve a Sudoku grid using a recursive backtracking algorithm.
    
    """

    def __init__(self, grid: SudokuGrid, validator: SudokuValidator):

        """
        Initialises SudokuRecursion with an instance of the SudokuGrid and SudokuValidator classes.

        Parameters:

            grid (SudokuGrid): The empty grid to be filled or the partially filled grid to be solved.
            validator (SudokuValidator): Validates grid operations to support the recursive process.

        """

        self.grid = grid
        self.validator = validator

    # RECURSIVE BACKTRACKING ALGORITHM

    def populate_grid(self) -> bool:

        """
        Fills the entire grid with a randomised number selection.

        Returns:

            bool: True if the grid was successfully filled, otherwise False.
        
        """

        # Traversal
        empty_cell = self.validator.find_next_empty_cell()

        # Base case
        if not empty_cell:

            return True
        


        row_index, col_index = empty_cell

        nums = list(range(1, 10))

        random.shuffle(nums)

        for num in nums:

            if self.validator.populate_cell(row_index, col_index, num):

                # Recursive step
                if self.populate_grid():

                    return True
                
                # Backtrack
                self.validator.reset_cell(row_index, col_index)

        return False
    
    def count_solutions(self) -> int:

        """
        Counts the total number of valid solutions to the grid.

        Returns:

            int: The total number of solutions to the grid.
        
        """

        # List ensures mutability throughout the recursive process.
        solutions = [0]

        def solve_sudoku() -> None:

            # Traversal
            empty_cell = self.validator.find_next_empty_cell()

            # Base case
            if not empty_cell:

                solutions[0] += 1

                # Do not return True; continue backtracking.
                return
            


            row_index, col_index = empty_cell
            
            for num in range(1, 10):

                if self.validator.populate_cell(row_index, col_index, num):

                    # Recursive step
                    solve_sudoku()

                    # Backtrack
                    self.validator.reset_cell(row_index, col_index)

        # Starts the recursive process.
        solve_sudoku()

        return solutions[0]
    
    def has_unique_solution(self) -> bool:

        """
        Checks if the grid has a unique solution.

        Returns:

            bool: True if the grid has a unique solution, otherwise False.
        
        """

        # Counts the number of solutions.
        solutions = 0

        def solve_sudoku() -> bool:

            nonlocal solutions

            # Traversal
            empty_cell = self.validator.find_next_empty_cell()

            # Base case
            if not empty_cell:

                solutions += 1

                # Stops the recursive process if more than one solution is found.
                return solutions <= 1
            


            row_index, col_index = empty_cell
            
            for num in range(1, 10):

                if self.validator.populate_cell(row_index, col_index, num):

                    # Recursive step
                    if not solve_sudoku():

                        # Stops the recursive process if more than one solution is found.
                        return False

                    # Backtrack
                    self.validator.reset_cell(row_index, col_index)

            return True

        # Starts the recursive process.
        solve_sudoku()

        return solutions == 1



if __name__ == "__main__":

    print("--------------------")

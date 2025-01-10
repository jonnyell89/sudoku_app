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
        
        self.nums = list(range(1, 10))

    # RECURSIVE BACKTRACKING ALGORITHM

    def populate_grid(self) -> bool:

        """
        Fills an empty or partially filled grid with a randomised number selection.

        Returns:

            bool: True if the grid was successfully filled, otherwise False.
        
        """

        # Traversal
        empty_cell = self.grid.find_next_empty_cell()

        # Base case, terminates recursion if no empty cells remain.
        if not empty_cell:

            return True
        


        row_index, col_index = empty_cell

        nums = self.nums[:]

        random.shuffle(nums)

        for num in nums:

            if self.validator.populate_cell(row_index, col_index, num):

                # Recursive step, continues to the next empty cell.
                if self.populate_grid():

                    return True
                
                # Backtrack
                self.grid.reset_cell(row_index, col_index)

        return False
    
    def is_solution_unique(self) -> int:

        """
        Checks if the grid has a single unique solution.

        Terminates when more than one solution is found.

        Returns:

            bool: True if the grid has a single unique solution, otherwise False.
        
        """

        if not self.validator.is_grid_valid():

            return False

        solutions = 0

        def solve_sudoku():

            nonlocal solutions

            if solutions > 1:

                return False

            # Traversal
            empty_cell = self.grid.find_next_empty_cell()

            # Base case, no empty cells remain.
            if not empty_cell:

                solutions += 1

                # Do not return True; continue backtracking.
                return
            


            row_index, col_index = empty_cell

            nums = self.nums[:]
            
            for num in nums:

                if self.validator.populate_cell(row_index, col_index, num):

                    # Recursive step, continue until all potential solutions are fully explored.
                    solve_sudoku()

                    # Backtracks, whether a solution is found or not.
                    self.grid.reset_cell(row_index, col_index)

        # Starts the recursive process.
        solve_sudoku()

        return solutions == 1
    
    def get_total_solutions(self, max_solutions: int = float("inf")) -> int:

        """
        Returns the total number of valid solutions to the grid.

        Continues counting until all potential solutions are fully explored.

        Parameters:

            max_solutions (int): Limits the number of solutions considering computational overhead.

        Returns:

            int: The total number of valid solutions to the grid.
        
        """

        if not self.validator.is_grid_valid():

            return False

        solutions = 0

        def solve_sudoku():

            nonlocal solutions

            # Traversal
            empty_cell = self.grid.find_next_empty_cell()

            # Base case, no empty cells remain.
            if not empty_cell:

                solutions += 1

                # Do not return True; continue backtracking.
                return
            


            row_index, col_index = empty_cell

            nums = self.nums[:]
            
            for num in nums:

                if self.validator.populate_cell(row_index, col_index, num):

                    if solutions >= max_solutions:

                        return

                    # Recursive step, continue until all potential solutions are fully explored.
                    solve_sudoku()

                    # Backtracks, whether a solution is found or not.
                    self.grid.reset_cell(row_index, col_index)

        # Starts the recursive process.
        solve_sudoku()

        return solutions

if __name__ == "__main__":

    print("--------------------")

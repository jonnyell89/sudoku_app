from typing import Tuple
import random

from app.grid import SudokuGrid
from app.validator import SudokuValidator
from app.recursion import SudokuRecursion

class SudokuGenerator:

    """
    A class to generate a Sudoku puzzle by removing cells from the Sudoku grid according to difficulty level.
    
    """

    def __init__(self, grid: SudokuGrid, validator: SudokuValidator, recursion: SudokuRecursion):

        """
        Initialises SudokuGenerator with an instance of the SudokuGrid and SudokuValidator classes.

        Parameters:

            grid (SudokuGrid): The grid to be transformed into a puzzle.
            validator (SudokuValidator): Validates grid operations to support the transformation process.
            recursion (SudokuRecursion): Ensures the puzzle has a unique solution.
        
        """

        self.grid = grid
        self.validator = validator
        self.recursion = recursion

    # CELL REMOVAL

    def remove_cells(self, difficulty_level: str) -> bool:

        """
        Removes cells from the grid according to the difficulty level.

        Parameters:

            difficulty_level (str): The difficulty level of the puzzle.
                
                Either "easy", "medium", "hard", or "expert".

        Raises:

            ValueError: If the difficulty level is invalid.

        Returns:

            bool: True if the cell removal process is successfully completed.
        
        """

        # Accesses the empty cell difficulty range according to difficulty level.
        difficulty_ranges = {

            "easy": (45, 49),
            "medium": (50, 54),
            "hard": (55, 58),
            "expert": (59, 64)

        }

        if difficulty_level not in difficulty_ranges:

            raise ValueError(f"Invalid difficulty level: {difficulty_level}")
        


        difficulty_range = difficulty_ranges[difficulty_level]

        target_removals = self.get_target_removals(difficulty_range)

        candidate_cells = self.grid.get_grid_indices()

        random.shuffle(candidate_cells)

        removable_cells = [(row_index, col_index) for row_index, col_index in candidate_cells if not self.validator.is_cell_empty(row_index, col_index)]

        removal_count = 0

        for row_index, col_index in removable_cells:

            # Break when the removal count matches the target removals.
            if removal_count >= target_removals:

                break

            # Removes the candidate cell and increments the removal count.
            if self._remove_cell(row_index, col_index):

                removal_count += 1
        
        return True
    
    def _remove_cell(self, row_index: int, col_index: int) -> bool:

        """
        Attempts to remove the candidate cell and checks that the grid remains valid.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the cell was removed and the grid remains valid, otherwise False.
        
        """

        # Stores the value of the candidate cell.
        candidate_cell = self.grid.grid[row_index][col_index]

        # Resets the candidate cell to zero.
        self.validator.reset_cell(row_index, col_index)

        # If the grid is valid.
        if self.recursion.count_solutions():

            return True

        # Otherwise, the candidate cell value is restored.
        else:

            self.grid.grid[row_index][col_index] = candidate_cell

            return False

    def get_target_removals(self, difficulty_range: Tuple[int, int]) -> int:

        """
        Returns the target number of cells to remove according to the difficulty range.

        Parameters:

            difficulty_range (Tuple[int, int]): The range of potential cell removals.

        Returns:

            target_removals (int): The target number of cells to remove.
        
        """

        min_remove, max_remove = difficulty_range

        # Randomly selects a number from within the difficulty level range.
        target_removals = random.randint(min_remove, max_remove)

        return target_removals



if __name__ == "__main__":

    print("--------------------")

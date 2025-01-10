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

    def generate_puzzle(self, target_removal: int = None, difficulty_level: str = None) -> bool:

        """
        Generates a Sudoku puzzle by determining the number of cells to remove from a complete Sudoku grid.

        Parameters:

            target_removal (int): The target number of cells to remove.
            difficulty_level (str): The difficulty level of the puzzle ('easy', 'medium', 'hard' or 'expert').

        Raises:

            ValueError: If both parameters are provided.
            ValueError: If the target number of cells is not a positive integer.
            ValueError: If the difficulty level is not a valid difficulty level.

        Returns:

            bool: True if the puzzle generation process is successfully completed.
        
        """

        if (target_removal is not None) and (difficulty_level is not None):

            raise ValueError("Please provide a target number of cells to remove or a valid difficulty level (e.g., easy, medium, hard or expert).")



        if target_removal is not None:

            self.validate_target_removal(target_removal)

            return self.remove_cells(target_removal)
        


        if difficulty_level is not None:

            difficulty_range = self.get_difficulty_range(difficulty_level)

            generated_target_removal = self.get_target_removal(difficulty_range)

            return self.remove_cells(generated_target_removal)



        raise ValueError("Please provide a target number of cells to remove or a valid difficulty level.")

    def validate_target_removal(self, target_removal: int) -> None:

        """
        Validates that the target number of cells to remove is a positive integer.

        Parameters:

            target_removal (int): The target number of cells to remove.
        
        Raises:

            ValueError: If the target number of cells to remove is not a positive integer.
        
        """

        if not isinstance(target_removal, int) or target_removal < 1:

            raise ValueError(f"{target_removal} must be a postive integer.")
        
    def get_target_removal(self, difficulty_range: Tuple[int, int]) -> int:

        """
        Returns the target number of cells to remove according to the difficulty range.

        Parameters:

            difficulty_range (Tuple[int, int]): The range of potential cell removals.

        Returns:

            int: The target number of cells to remove.
        
        """

        min_remove, max_remove = difficulty_range

        # Randomly selects a number from within the difficulty level range.
        return random.randint(min_remove, max_remove)
        
    def get_difficulty_range(self, difficulty_level: str) -> Tuple[int, int]:

        """
        Returns the difficulty range according to the difficulty level.

        Parameters:

            difficulty_level (str): The difficulty level of the puzzle ('easy', 'medium', 'hard' or 'expert').
        
        Raises:

            ValueError: If the difficulty level is not a valid difficulty level.

        Returns:

            Tuple[int, int]: The difficulty range according to difficulty level.
        
        """

        difficulty_ranges = {

            "easy": (45, 49),
            "medium": (50, 54),
            "hard": (55, 58),
            "expert": (59, 64)

        }

        if difficulty_level not in difficulty_ranges:

            raise ValueError(f"Please provide a valid difficulty level (e.g., easy, medium, hard or expert).")
        
        return difficulty_ranges[difficulty_level]

    def remove_cells(self, target_removal: int) -> bool:

        """
        Removes the target number of cells from the grid.

        Parameters:

            target_removal (int): The number of cells to be removed from the grid.

        Returns:

            bool: True if the cell removal process is successfully completed.
        
        """

        print(f"Target removal: {target_removal}")

        removable_cells = self.grid.get_removable_cell_indices()

        print(f"Number of removable cells: {len(removable_cells)}")

        random.shuffle(removable_cells)

        removal_count = 0

        for row_index, col_index in removable_cells:

            if removal_count >= target_removal:

                break

            if self._remove_cell(row_index, col_index):

                removal_count += 1

                print(f"Removal successful: {removal_count}/{target_removal}")
        
        return True
    
    def _remove_cell(self, row_index: int, col_index: int) -> bool:

        """
        Attempts to remove the specified cell and checks that the grid remains valid.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the cell was removed and the grid remains valid, otherwise False.
        
        """

        # Stores the value of the removable cell.
        removable_cell = self.grid.grid[row_index][col_index]

        print(f"Trying to remove cell at: ({row_index, col_index})")

        # Resets the removable cell to zero.
        self.grid.reset_cell(row_index, col_index)

        # If the grid is valid.
        if self.recursion.is_solution_unique():

            return True

        # Otherwise, the removable cell value is restored.
        else:

            print(f"Restoring cell at: ({row_index, col_index})")

            self.grid.grid[row_index][col_index] = removable_cell

            print(f"Empty cells remaining: {self.grid.count_empty_cells()}")

            return False



if __name__ == "__main__":

    print("--------------------")

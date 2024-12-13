from typing import List, Tuple, Dict, Callable, Any, Iterable
import random

from test.test_grids import empty_grid, valid_grid, invalid_row, invalid_col, invalid_subgrid, easy_grid, medium_grid, hard_grid, expert_grid, master_grid, extreme_grid, brute_force

class Sudoku:

    """
    A class for creating, managing and solving a 9X9 Sudoku grid.
    
    """

    def __init__(self, grid=None) -> None:

        """
        Initialises the grid input, or generates an empty grid, if none is provided.
        
        """

        self.grid = grid or [[0 for _ in range(9)] for _ in range(9)]

    # PRINT

    def print_grid(self) -> None:

        """
        Prints the grid as a two-dimensional matrix, with numbers separated by spaces.
        
        """

        for row in self.grid:

            print(" ".join(str(num) for num in row))

    def print_formatted_grid(self) -> None:

        """
        Prints the grid as a two-dimensional matrix, with visual separators forming nine 3X3 subgrids.
        
        """

        for row_index in range(len(self.grid)):

            # Prints inner horizontal subgrid construction lines.
            if row_index > 0 and row_index % 3 == 0:

                print("-" * 15)

            for col_index in range(len(self.grid)):

                # Prints inner vertical subgrid construction lines.
                if col_index > 0 and col_index % 3 == 0:

                    print(" | ", end="")

                if col_index == len(self.grid) - 1:

                    # Ensures a new line after printing last cell in row.
                    print(self.grid[row_index][col_index])

                else:

                    # Ensures each cell is printed on the same line.
                    print(self.grid[row_index][col_index], end="")

    # GET INITS

    def get_row(self, row_index: int) -> List[int]:

        """
        Returns a specific row from the grid.

        Parameters:

            row_index (int): The index position of the row in the two-dimensional list matrix.

        Raises:

            ValueError: If row_index is out of the specified range.

        Returns:

            List[int]: A list of integers representing a specific row from the grid.
        
        """

        if row_index not in range(9):

            raise ValueError(f"row_index {row_index} must be within range 0 to 8.")



        return self.grid[row_index]
    
    def get_col(self, col_index: int) -> List[int]:

        """
        Returns a specific column from the grid.

        Parameters:

            col_index (int): The index position of the column in the two-dimensional list matrix.

        Raises:

            ValueError: If col_index is out of the specified range.

        Returns:

            List[int]: A list of integers representing a specific column from the grid.
        
        """

        if col_index not in range(9):

            raise ValueError(f"col_index {col_index} must be within range 0 to 8.")
        


        return [row[col_index] for row in self.grid]
    
    def get_subgrid(self, indices: Tuple[int, int]) -> List[int]:

        """
        Returns the subgrid containing the specified cell.

        Parameters:

            indices (Tuple[int, int]): The row and col indices in the two-dimensional list matrix.

        Raises:

            ValueError: If indices are out of the specified range.

        Returns:

            List[int]: A list of integers representing a specific subgrid from the grid.
        
        """

        row_index, col_index = indices

        if row_index not in range(9) or col_index not in range(9):

            raise ValueError(f"row_index {row_index} and col_index {col_index} must be within range 0 to 8.")



        start_row = (row_index // 3) * 3
        start_col = (col_index // 3) * 3

        return [self.grid[start_row + x][start_col + y] for x in range(3) for y in range(3)]
    
    # RECURSIVE BACKTRACK UTILITIES

    def is_valid(self, indices: Tuple[int, int], num: int) -> bool:

        """
        Checks if a number placement at the specified indices is valid within the rules of Sudoku.

        Parameters:

            indices (Tuple[int, int]): The row and col indices in the two-dimensional list matrix.
            num (int): The number to be checked, between 1 and 9.

        Raises:

            ValueError: If indices are out of the specified range.

        Returns:

            bool: True if the number placement is valid, otherwise False.
            
        """

        row_index, col_index = indices

        if row_index not in range(9) or col_index not in range(9):

            raise ValueError(f"row_index {row_index} col_index {col_index} must be within range 0 to 8.")

        if num not in range(1, 10):

            raise ValueError(f"num {num} must be within range 1 to 9.")
        


        row = self.get_row(row_index)

        col = self.get_col(col_index)

        subgrid = self.get_subgrid(indices)

        # Returns True if num is in row or num is in col or num is in subgrid
        return num not in row and num not in col and num not in subgrid

    def populate_cell(self, indices: Tuple[int, int], num: int) -> bool:

        """
        Places a number at the specified indices if the placement is valid and the cell is empty.

        Parameters:

            indices (Tuple[int, int]): The row and col indices in the two-dimensional list matrix.
            num (int): The number to be placed, between 1 and 9.
        
        Returns:

            bool: True if the number placement was successful, otherwise False.

        """

        row_index, col_index = indices

        if self.is_valid(indices, num) and self.grid[row_index][col_index] == 0:

            self.grid[row_index][col_index] = num

            return True
        
        return False

    def reset_cell(self, indices: Tuple[int, int]) -> None:
        
        """
        Resets the cell to zero at the specified indices.

        Parameters:

            indices (Tuple[int, int]): The row and col indices in the two-dimensional list matrix.
        
        """

        row_index, col_index = indices

        self.grid[row_index][col_index] = 0

    def find_next_empty_cell(self) -> Tuple[int, int]:

        """
        Finds the next empty cell in the grid.

        Returns:

            Tuple[int, int]: The row and col indices of the next empty cell, or None if all cells are full.
        
        """

        for row_index in range(len(self.grid)):

            for col_index in range(len(self.grid)):

                if self.grid[row_index][col_index] == 0:

                    return (row_index, col_index)
                
        return None

    # RECURSIVE BACKTRACK ALGORITHM

    def populate_grid(self) -> bool:

        """
        Fills the entire grid using a recursive backtracking algorithm.

        Returns:

            bool: True if the grid was successfully filled, otherwise False.
        
        """

        # Traversal
        empty_cell = self.find_next_empty_cell()

        # Base case
        if not empty_cell:

            return True



        nums = list(range(1, 10))

        random.shuffle(nums)

        for num in nums:

            if self.populate_cell(empty_cell, num):

                # Recursive step
                if self.populate_grid():

                    return True
                
                # Backtrack
                self.reset_cell(empty_cell)

        return False
    
    def count_solutions(self) -> int:

        """
        Counts the number of valid solutions to the grid using the recursive backtracking algorithm.

        Returns:

            int: The total number of valid solutions to the grid.
        
        """

        # List ensures mutability throughout the recursive process.
        solutions = [0]

        def solve_sudoku() -> bool:

            # Traversal
            empty_cell = self.find_next_empty_cell()

            # Base case
            if not empty_cell:

                solutions[0] += 1

                # Do not return True; continue backtracking.
                return
            
            for num in range(1, 10):

                if self.populate_cell(empty_cell, num):

                    # Recursive step
                    solve_sudoku()

                    # Backtrack
                    self.reset_cell(empty_cell)

        # Starts the recursive process.
        solve_sudoku()

        return solutions[0]
    
    # VALIDATION

    def is_grid_valid(self, debug: bool = False) -> bool:

        """
        Checks that all rows, columns and subgrids are valid within the rules of Sudoku.

        Parameters:

            debug (bool): If True, returns detailed information about any invalid units.

        Returns:

            bool or Dict[str, Any]: False if the grid is invalid. If debug is True, returns a dictionary containing the invalid units.
        
        """

        invalid_units = {unit_type: {} for unit_type, _, _ in self._get_units()}

        for unit_type, get_unit, indices in self._get_units():

            for index in indices:

                unit = get_unit(index)

                if not self.is_unit_valid(unit):
                        
                    invalid_units[unit_type][index] = unit

        has_invalid_units = any(invalid_units[unit_type] for unit_type in invalid_units)

        if has_invalid_units:

            if debug:
                
                return {"is_valid": False, "invalid_units": invalid_units}
            
            else:

                return False
            
        return True
    
    def is_unit_valid(self, unit: List[int]) -> bool:

        """
        Checks that a single unit contains unique numbers only.

        Parameters:

            unit (List[int]): A list of integers representing a single row, column or subgrid.
        
        Returns:

            bool: True if the unit is valid, otherwise False.
        
        """

        nums = set()

        for num in unit:

            if num > 0:

                if num in nums:

                    return False
                
                nums.add(num)

        return True
    
    def _get_units(self) -> List[Tuple[str, Callable, Iterable[int]]]:

        """
        Helper Method: Returns the information required to access all rows, columns and subgrids.

        Returns:

            List[Tuple[str, Callable, Iterable[int]]]: A list of unit descriptors, consisting of their types, methods and indices.
        
        """

        units = [

            ("rows", self.get_row, range(9)),
            ("cols", self.get_col, range(9)),
            ("subgrids", self.get_subgrid, self._subgrid_indices())

        ]

        return units

    def _subgrid_indices(self) -> List[Tuple[int, int]]:

        """
        Helper method: Provides the indices for the top-left cell in each individual subgrid.

        Returns:

            List[Tuple[int, int]]: A list of tuples representing the starting indices of each subgrid.
        
        """

        return [(x, y) for x in (0, 3, 6) for y in (0, 3, 6)]

    # CELL REMOVAL

    def count_empty_cells(self):

        """
        Counts the total number of empty cells in the grid.

        Returns:

            int: The total number of cells with the value of zero.
        
        """

        empty_cells = 0
            
        for row_index in range(len(self.grid)):
            
            for col_index in range(len(self.grid)):

                if self.grid[row_index][col_index] == 0:

                    empty_cells += 1

        return empty_cells
    


    """
    def remove_cells(self, difficulty_level):

        difficulty_levels = {

            "easy": (36, 50),
            "medium": (50, 55),
            "hard": (55, 60),
            "expert": (60, 70)

        }[difficulty_level]

        if not difficulty_levels:

            raise ValueError(f"difficulty_level {difficulty_level} must be a valid dictionary key.")

        i, j = difficulty_levels

        cells_to_remove = random.randint(i, j)

    """



    def remove_cells(self, difficulty_level):

        # Directly accesses the difficulty level.
        difficulty_levels = {

            "easy": (36, 50),
            "medium": (50, 55),
            "hard": (55, 60),
            "expert": (60, 70)

        }[difficulty_level]

        if not difficulty_levels:

            raise ValueError(f"difficulty_level {difficulty_level} must be a valid dictionary key.")

        # Unpacks the difficulty level range.
        i, j = difficulty_levels

        # Randomly selects a number from within the difficulty level range.
        cells_to_remove = random.randint(i, j)

        # Generates all grid indices.
        grid_indices = [(row_index, col_index) for row_index in range(9) for col_index in range(9)]

        # Randomly shuffles the grid indices.
        random.shuffle(grid_indices)

        # Iterates over the unpacked grid indices.
        for row_index, col_index in grid_indices:

            # Break when the number of cells left to remove reaches zero.
            if cells_to_remove == 0:

                break

            # Stores the value at that specific cell.
            temp = self.grid[row_index][col_index]

            # Packs the grid indices.
            indices = (row_index, col_index)

            # Resets the specific cell to zero.
            self.reset_cell(indices)

            # If there is more or less than one solution, restore the stored value.
            if not self.count_solutions() == 1:

                self.grid[row_index][col_index] = temp

            # Otherwise, decrement the number of cells to remove.
            else:

                cells_to_remove -= 1

        # Returns True when the entire process is finished.
        return True



if __name__ == "__main__":

    print("--------------------")

    sudoku = Sudoku(grid=master_grid)

    sudoku.populate_grid()

    sudoku.print_formatted_grid()

    print("--------------------")

    sudoku.remove_cells("medium")

    sudoku.print_formatted_grid()

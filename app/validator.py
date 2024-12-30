from typing import List, Tuple, Iterable, Callable

from app.grid import SudokuGrid

class SudokuValidator:

    """
    A class to validate cell placements and the overall integrity of a Sudoku grid.
    
    """

    def __init__(self, grid: SudokuGrid):

        """
        Initialises SudokuValidator with an instance of the SudokuGrid class.

        Parameters:

            grid (SudokuGrid): The grid to be validated.
        
        """

        self.grid = grid

    # CELL VALIDATION

    def is_valid(self, row_index: int, col_index: int, num: int) -> bool:

        """
        Checks if a number placement at the specified indices is valid within the rules of Sudoku.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
            num (int): The number to be checked, between 1 and 9.

        Raises:

            ValueError: If indices are out of the specified range.

        Returns:

            bool: True if the number placement is valid, otherwise False.
            
        """

        if row_index not in range(9) or col_index not in range(9):

            raise ValueError(f"row_index {row_index} col_index {col_index} must be within range 0 to 8.")

        if num not in range(1, 10):

            raise ValueError(f"num {num} must be within range 1 to 9.")
        
        containing_values = self.grid.get_containing_values(row_index, col_index)
                
        return num not in containing_values

    def populate_cell(self, row_index: int, col_index: int, num: int) -> bool:

        """
        Attempts to place a number at the specified indices if the placement is valid and the cell is empty.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
            num (int): The number to be placed, between 1 and 9.
        
        Returns:

            bool: True if the number placement was successful, otherwise False.

        """

        if self.is_cell_empty(row_index, col_index) and self.is_valid(row_index, col_index, num):

            self.grid.grid[row_index][col_index] = num

            return True
        
        return False

    def reset_cell(self, row_index: int, col_index: int) -> None:
        
        """
        Resets the cell to zero at the specified indices.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
        
        """

        self.grid.grid[row_index][col_index] = 0

    def is_cell_empty(self, row_index: int, col_index: int) -> bool:

        """
        Checks if the specified cell is already empty.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the specified cell is already empty, otherwise False.
        
        """

        return self.grid.grid[row_index][col_index] == 0

    def find_next_empty_cell(self) -> Tuple[int, int]:

        """
        Finds the next empty cell in the grid.

        Returns:

            Tuple[int, int]: The row and column indices of the next empty cell, or None if all cells are full.
        
        """

        for row_index in range(len(self.grid.grid)):

            for col_index in range(len(self.grid.grid)):

                if self.is_cell_empty(row_index, col_index):

                    return (row_index, col_index)
                
        return None
    
    def count_empty_cells(self) -> int:

        """
        Counts the total number of empty cells in the grid.

        Returns:

            int: The total number of cells with the value of zero.
        
        """

        empty_cells = 0
            
        for row_index in range(len(self.grid.grid)):
            
            for col_index in range(len(self.grid.grid)):

                if self.is_cell_empty(row_index, col_index):

                    empty_cells += 1

        return empty_cells
    
    # GRID VALIDATION

    def is_grid_valid(self, debug: bool = False) -> bool:

        """
        Checks that all rows, columns and subgrids are valid within the rules of Sudoku.

        Parameters:

            debug (bool): If True, returns detailed information about any invalid units.

        Returns:

            bool or Dict[str, Any]: False if the grid is invalid, or if debug is True, returns a dictionary containing the invalid units.
        
        """

        invalid_units = {unit_type: {} for unit_type, _, _ in self._get_units()}

        for unit_type, get_unit, indices in self._get_units():

            for index in indices:

                if isinstance(index, tuple):

                    row_index, col_index = index

                    unit = get_unit(row_index, col_index)
                
                else:

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
    
    def _get_units(self) -> List[Tuple[str, Callable, Iterable[int]]]:

        """
        Returns the information required to access all rows, columns and subgrids.

        Returns:

            List[Tuple[str, Callable, Iterable[int]]]: A list of unit descriptors, consisting of their types, access methods and indices.
        
        """

        units = [

            ("rows", self.grid.get_row, range(9)),
            ("cols", self.grid.get_col, range(9)),
            ("subgrids", self.grid.get_subgrid, self.grid.get_subgrid_indices())

        ]

        return units
    
    def is_unit_valid(self, unit: List[int]) -> bool:

        """
        Checks if a row, column or subgrid contains unique numbers only.

        Parameters:

            unit (List[int]): A list of integers representing a row, column or subgrid.
        
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



if __name__ == "__main__":

    print("--------------------")

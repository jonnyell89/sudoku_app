from typing import List, Tuple, Iterable, Callable

from app.grid import SudokuGrid
from config.config import GRID_SIZE

class SudokuValidator:

    """
    A class to validate number placements and the overall integrity of a Sudoku grid.
    
    """

    def __init__(self, grid: SudokuGrid):

        """
        Initialises SudokuValidator with an instance of the SudokuGrid class.

        Parameters:

            grid (SudokuGrid): The grid to be validated.
        
        """

        self.grid = grid

    def populate_cell(self, row_index: int, col_index: int, num: int) -> bool:

        """
        Attempts to place a number at the specified indices if the cell is empty and the placement is valid.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
            num (int): The number to be placed, between 1 and 9.
        
        Returns:

            bool: True if the number placement was successful, otherwise False.

        """

        if self.grid.is_cell_empty(row_index, col_index) and self.is_valid(row_index, col_index, num):

            self.grid.grid[row_index][col_index] = num

            return True
        
        return False

    def is_valid(self, row_index: int, col_index: int, num: int) -> bool:

        """
        Checks if a number placement at the specified indices is valid within the rules of Sudoku.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
            num (int): The number to be checked, between 1 and 9.

        Returns:

            bool: True if the number placement is valid, otherwise False.
            
        """

        containing_values = self.grid.get_containing_values(row_index, col_index)
                
        return num not in containing_values
    
    def is_grid_valid(self, debug: bool = False) -> bool:

        """
        Checks that all rows, columns and subgrids are valid within the rules of Sudoku.

        Parameters:

            debug (bool): If True, returns detailed information about any invalid units.

        Returns:

            bool or Dict[str, Any]: False if the grid is invalid, or if debug is True, returns a dictionary containing the invalid units.
        
        """

        invalid_units = {unit_type: {} for unit_type, _, _ in self._get_all_units()}

        for unit_type, get_unit, indices in self._get_all_units():

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
    
    def _get_all_units(self) -> List[Tuple[str, Callable, Iterable[int]]]:

        """
        Returns the information required to access all rows, columns and subgrids.

        Returns:

            List[Tuple[str, Callable, Iterable[int]]]: A list of unit descriptors, consisting of their types, access methods and indices.
        
        """

        units = [

            ("rows", self.grid.get_row, range(GRID_SIZE)),
            ("cols", self.grid.get_col, range(GRID_SIZE)),
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

from typing import List, Tuple, Dict, Callable

from app.grid import SudokuGrid
from app.validator import SudokuValidator

class SudokuIteration:

    """
    A class to solve a Sudoku puzzle using logical deduction technqiues employed by human players.
    
    """

    def __init__(self, grid: SudokuGrid, validator: SudokuValidator):

        """
        Initialises SudokuIteration with an instance of the SudokuGrid and SudokuValidator classes.

        Parameters:

            grid (SudokuGrid): The partially filled grid to be solved.
            validator (SudokuValidator): Validates grid operations to support the iterative process.
        
        """

        self.grid = grid
        self.validator = validator

    # LOGICAL DEDUCTION

    def placement_techniques(self) -> Dict[str, Dict[str, List]]:

        """
        Applies all logical deduction placement techniques, and records all successful placements.

        Returns:

            Dict[str, Dict[str, Union[int, List[Tuple[int, int]]]]]: 
            
                A dictionary where the keys are technique names and the values are nested dictionaries containing:

                    "count": The number of successful placements (int).
                    "indices": A list of the indices for each successful placement (List[Tuple[int, int]]).
        
        """

        placement_techniques = {technique_type: {"count": 0, "indices": []} for technique_type, _ in self._get_techniques()}

        rotations = 0

        while True:

            placement_made = False

            for technique_type, technique_method in self._get_techniques():

                # Refreshes the list of empty cell indices after every technique method.
                empty_cell_indices = self.grid.get_empty_cell_indices()

                if not empty_cell_indices:

                    break

                successful_indices = []

                for row_index, col_index in empty_cell_indices:

                    if technique_method(row_index, col_index):

                        successful_indices.append((row_index, col_index))

                        placement_made = True

                placement_techniques[technique_type]["count"] += len(successful_indices)
                placement_techniques[technique_type]["indices"].extend(successful_indices)

            rotations += 1

            remaining_cells = self.validator.count_empty_cells()
            
            if not placement_made or remaining_cells == 0:

                print(f"There are {remaining_cells} cells remaining after {rotations} placement technique rotations.")

                break

        return placement_techniques
    
    def _get_techniques(self) -> List[Tuple[str, Callable]]:

        """
        Returns a list of tuples containing the logical deduction placement techniques.

        Each tuple consists of:

            The name of the technique (str).
            The corresponding method to apply the technique (Callable).

        Returns:

            List[Tuple[str, Callable]]: A list of logical deduction placement techniques.
        
        """

        techniques = [

            ("naked_single", self.naked_single),
            ("low_hanging_fruit", self.low_hanging_fruit),
            ("placement_by_adjacent_units", self.placement_by_adjacent_units)

        ]

        return techniques



    def naked_single(self, row_index: int, col_index: int) -> bool:

        """
        Attempts to fill an empty cell using the 'naked single' technique.

        A naked single is a cell that has only one possible value based on the numbers already present in its containing row, column and subgrid.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the cell was successfully filled, otherwise False.
        
        """

        if not self.validator.is_cell_empty(row_index, col_index):

            return False

        containing_values = self.grid.get_containing_values(row_index, col_index)

        remaining_values = self.grid.get_remaining_values(containing_values)

        only_remaining_option = self.only_remaining_option(row_index, col_index, remaining_values)

        return only_remaining_option
    
    def only_remaining_option(self, row_index: int, col_index: int, remaining_values: List[int]) -> bool:

        """
        Attempts to place a value in the specified cell, if that value is the only possible value.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
            remaining_values (List[int]): A list of all remaining potential values for the specified cell.

        Returns:

            bool: True if the cell was successfully filled, otherwise False.
        
        """

        if len(remaining_values) == 1:
            
            self.validator.populate_cell(row_index, col_index, remaining_values[0])

            return True
        
        return False
    
    def low_hanging_fruit(self, row_index: int, col_index: int) -> bool:

        """
        Attempts to fill an empty cell if there is only one remaining option in any of its containing row, column or subgrid.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the cell was successfully filled, otherwise False.
        
        """

        units = [
            
            self.grid.get_subgrid(row_index, col_index), 
            self.grid.get_row(row_index), 
            self.grid.get_col(col_index)
            
        ]

        for unit in units:

            remaining_values = self.grid.get_remaining_values(unit)

            if self.only_remaining_option(row_index, col_index, remaining_values):

                return True
            
        return False
    
    def placement_by_adjacent_units(self, row_index: int, col_index: int) -> bool:

        """
        Attempts to fill an empty cell if there is only one remaining option due to the values present in the adjacent rows and columns.
        
        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the cell was successfully filled, otherwise False.

        """

        containing_values = self.grid.get_containing_values(row_index, col_index)

        remaining_values = self.grid.get_remaining_values(containing_values)

        adjacent_rows, adjacent_cols = self.get_adjacent_units(row_index, col_index)

        for value in remaining_values:

            if value in adjacent_rows[0] and value in adjacent_rows[1] and value in adjacent_cols[0] and value in adjacent_cols[1]:

                self.validator.populate_cell(row_index, col_index, value)
    
                return True

        return False
    
    def get_adjacent_units(self, row_index: int, col_index: int) -> List[List[int]]:

        """
        Returns the values present in the adjacent rows and columns of the specified cell.

        The adjacent units do not include the containing units.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            List[List[int]]: A list of the adjacent rows and columns of the specifed cell.
        
        """

        start_row = (row_index // 3) * 3
        start_col = (col_index // 3) * 3

        adjacent_rows = [self.grid.get_row(start_row + index) for index in range(3) if (start_row + index) != row_index]

        adjacent_cols = [self.grid.get_col(start_col + index) for index in range(3) if (start_col + index) != col_index]

        return adjacent_rows, adjacent_cols

    def get_containing_units(self, row_index: int, col_index: int) -> List[List[int]]:

        """
        Returns the values present in the containing rows, columns and subgrid of the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            List[List[int]]: A list of the containing rows, columns and subgrid of the specified cell.
        
        """

        start_row = (row_index // 3) * 3
        start_col = (col_index // 3) * 3

        containing_rows = [self.grid.get_row(start_row + index) for index in range(3)]

        containing_cols = [self.grid.get_col(start_col + index) for index in range(3)]

        containing_subgrid = self.grid.get_subgrid(row_index, col_index)

        return containing_subgrid, containing_rows, containing_cols



    def populate_remaining_values_dict(self):

        for row_index, col_index in self.grid.remaining_values_dict.keys():

            if not self.validator.is_cell_empty(row_index, col_index):

                continue

            containing_values = self.grid.get_containing_values(row_index, col_index)

            remaining_values = self.grid.get_remaining_values(containing_values)

            self.grid.remaining_values_dict[(row_index, col_index)].extend(remaining_values)



if __name__ == "__main__":

    print("--------------------")

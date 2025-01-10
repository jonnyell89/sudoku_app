from typing import List, Tuple

from config.config import GRID_SIZE, SUBGRID_SIZE

class SudokuGrid:

    """
    A class to manage access to a Sudoku grid.
    
    """

    def __init__(self, grid: List[List[int]] = None) -> None:

        """
        Initialises SudokuGrid with an optional grid input, or generates an empty grid, if None is provided.
        
        """

        self.grid = grid or [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.original = [row[:] for row in self.grid]

    def get_row(self, row_index: int) -> List[int]:

        """
        Returns the specified row from the grid.

        Parameters:

            row_index (int): The index position of the row in the grid.

        Returns:

            List[int]: A list of integers representing the specified row from the grid.
        
        """

        return self.grid[row_index]
    
    def get_col(self, col_index: int) -> List[int]:

        """
        Returns the specified column from the grid.

        Parameters:

            col_index (int): The index position of the column in the grid.

        Returns:

            List[int]: A list of integers representing the specified column from the grid.
        
        """

        return [row[col_index] for row in self.grid]
    
    def get_subgrid(self, row_index: int, col_index: int) -> List[int]:

        """
        Returns the subgrid containing the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            List[int]: A list of integers representing the specified subgrid from the grid.
        
        """

        start_row = (row_index // SUBGRID_SIZE) * SUBGRID_SIZE
        start_col = (col_index // SUBGRID_SIZE) * SUBGRID_SIZE

        return [self.grid[start_row + x][start_col + y] for x in range(SUBGRID_SIZE) for y in range(SUBGRID_SIZE)]

    def get_containing_values(self, row_index: int, col_index: int) -> List[int]:

        """
        Returns the values present in the containing row, column and subgrid of the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            List[int]: A list of the values present in the containing row, column and subgrid of the specified cell.
        
        """

        return list(set(self.get_row(row_index)) | set(self.get_col(col_index)) | set(self.get_subgrid(row_index, col_index)))

    def get_remaining_values(self, containing_values: List[int]) -> List[int]:

        """
        Returns all remaining potential values for a specified cell.

        Parameters:

            containing_values (List[int]): A list of the values present in the containing row, column and subgrid of a specified cell.

        Returns:

            List[int]: A list of all remaining potential values for a specified cell.
        
        """

        return [num for num in range(1, 10) if num not in containing_values]
    
    def possible_values(self, row_index, col_index) -> List[int]:

        """
        Returns all possible values for the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            List[int]: A list of all possible values for the specified cell.
        
        """

        return self.get_remaining_values(self.get_containing_values(row_index, col_index))
    
    def is_cell_empty(self, row_index: int, col_index: int) -> bool:

        """
        Checks if the specified cell is empty.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            bool: True if the specified cell is empty, otherwise False.
        
        """

        return self.grid[row_index][col_index] == 0
    
    def reset_cell(self, row_index: int, col_index: int) -> None:
        
        """
        Resets the cell to zero at the specified indices.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.
        
        """

        self.grid[row_index][col_index] = 0
    
    def count_empty_cells(self) -> int:

        """
        Counts the total number of empty cells in the grid.

        Returns:

            int: The total number of cells with the value of zero.
        
        """

        empty_cells = 0
            
        for row_index in range(GRID_SIZE):
            
            for col_index in range(GRID_SIZE):

                if self.is_cell_empty(row_index, col_index):

                    empty_cells += 1

        return empty_cells
    
    def find_next_empty_cell(self) -> Tuple[int, int]:

        """
        Finds the next empty cell in the grid.

        Returns:

            Tuple[int, int]: The row and column indices of the next empty cell, or None if all cells are full.
        
        """

        for row_index in range(GRID_SIZE):

            for col_index in range(GRID_SIZE):

                if self.is_cell_empty(row_index, col_index):

                    return (row_index, col_index)
                
        return None

    def get_grid_indices(self) -> List[Tuple[int, int]]:

        """
        Returns a list of indices for every cell in the grid.

        Returns:

            List[Tuple[int, int]]: A list of indices for every cell in the grid.
        
        """

        return [(row_index, col_index) for row_index in range(GRID_SIZE) for col_index in range(GRID_SIZE)]

    def get_subgrid_indices(self) -> List[Tuple[int, int]]:

        """
        Returns the indices for the top-left cell in each individual subgrid.

        Returns:

            List[Tuple[int, int]]: A list of tuples representing the starting indices of each subgrid.
        
        """

        return [(row_index, col_index) for row_index in (0, 3, 6) for col_index in (0, 3, 6)]
    
    def get_empty_cell_indices(self) -> List[Tuple[int, int]]:

        """
        Returns the row and column indices for all remaining empty cells in the grid.

        Returns:

            List[Tuple[int, int]]: A list of tuples containing the row and column indices for all remaining empty cells in the grid.
        
        """

        return [(row_index, col_index) for row_index in range(GRID_SIZE) for col_index in range(GRID_SIZE) if self.is_cell_empty(row_index, col_index)]
    
    def get_removable_cell_indices(self) -> List[Tuple[int, int]]:

        """
        Returns the row and column indices for all removable cells in the grid.

        Returns:

            List[Tuple[int, int]]: A list of tuples containing the row and column indices for all removable cells in the grid.
        
        """

        return [(row_index, col_index) for row_index in range(GRID_SIZE) for col_index in range(GRID_SIZE) if not self.is_cell_empty(row_index, col_index)]



if __name__ == "__main__":

    print("--------------------")

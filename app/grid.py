from typing import List, Tuple, Set

class SudokuGrid:

    """
    A class to manage access to a 9X9 Sudoku grid.
    
    """

    def __init__(self, grid=None) -> None:

        """
        Initialises SudokuGrid with an optional grid input, or generates an empty grid, if None is provided.
        
        """

        self.grid = grid or [[0 for _ in range(9)] for _ in range(9)]

        self.remaining_values_dict = {(row_index, col_index): [] for (row_index, col_index) in self.get_grid_indices()}

    # PRINT

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
        Returns the specified row from the grid.

        Parameters:

            row_index (int): The index position of the row in the grid.

        Raises:

            ValueError: If row_index is out of the specified range.

        Returns:

            List[int]: A list of integers representing the specified row from the grid.
        
        """

        if row_index not in range(9):

            raise ValueError(f"row_index {row_index} must be within range 0 to 8.")



        return self.grid[row_index]
    
    def get_col(self, col_index: int) -> List[int]:

        """
        Returns the specified column from the grid.

        Parameters:

            col_index (int): The index position of the column in the grid.

        Raises:

            ValueError: If col_index is out of the specified range.

        Returns:

            List[int]: A list of integers representing the specified column from the grid.
        
        """

        if col_index not in range(9):

            raise ValueError(f"col_index {col_index} must be within range 0 to 8.")
        


        return [row[col_index] for row in self.grid]
    
    def get_subgrid(self, row_index: int, col_index: int) -> List[int]:

        """
        Returns the subgrid containing the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Raises:

            ValueError: If indices are out of the specified range.

        Returns:

            List[int]: A list of integers representing the specified subgrid from the grid.
        
        """

        if row_index not in range(9) or col_index not in range(9):

            raise ValueError(f"row_index {row_index} and col_index {col_index} must be within range 0 to 8.")



        start_row = (row_index // 3) * 3
        start_col = (col_index // 3) * 3

        return [self.grid[start_row + x][start_col + y] for x in range(3) for y in range(3)]



    def get_containing_values(self, row_index: int, col_index: int) -> Set[int]:

        """
        Returns the values present in the containing row, column and subgrid of the specified cell.

        Parameters:

            row_index (int): The index position of the row in the grid.
            col_index (int): The index position of the column in the grid.

        Returns:

            Set[int]: A set of the values present in the containing row, column and subgrid of the specified cell.
        
        """

        containing_values = set(self.get_row(row_index)) | set(self.get_col(col_index)) | set(self.get_subgrid(row_index, col_index))

        return containing_values

    def get_remaining_values(self, containing_values: List[int]) -> List[int]:

        """
        Returns all remaining potential values for the specified cell.

        Parameters:

            containing_values (List[int]): A list of the values present in the containing row, column and subgrid of the specified cell.

        Returns:

            List[int]: A list of all remaining potential values for the specified cell.
        
        """

        remaining_values = [num for num in range(1, 10) if num not in containing_values]

        return remaining_values



    def get_grid_indices(self) -> List[Tuple[int, int]]:

        """
        Generates a list of indices for every cell in the grid.

        Returns:

            List[Tuple[int, int]]: A list of indices for every cell in the grid.
        
        """

        grid_indices = [(row_index, col_index) for row_index in range(len(self.grid)) for col_index in range(len(self.grid))]

        return grid_indices

    def get_subgrid_indices(self) -> List[Tuple[int, int]]:

        """
        Returns the indices for the top-left cell in each individual subgrid.

        Returns:

            List[Tuple[int, int]]: A list of tuples representing the starting indices of each subgrid.
        
        """

        subgrid_indices = [(row_index, col_index) for row_index in (0, 3, 6) for col_index in (0, 3, 6)]

        return subgrid_indices

    def get_empty_cell_indices(self) -> List[Tuple[int, int]]:

        """
        Returns the row and column indices for all remaining empty cells in the grid.

        Returns:

            List[Tuple[int, int]]: A list of tuples containing the row and column indices for all remaining empty cells in the grid.
        
        """

        empty_cell_indices = [(row_index, col_index) for row_index in range(len(self.grid)) for col_index in range(len(self.grid)) if self.grid[row_index][col_index] == 0]

        return empty_cell_indices



if __name__ == "__main__":

    print("--------------------")
